import random
import math

class NeuralNetTrainer:
	def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
		self.input_size = input_size
		self.hidden_size = hidden_size
		self.output_size = output_size
		self.learning_rate = learning_rate
		
		# Initialize weights
		self.weights_input_hidden = [[random.uniform(-1, 1) for _ in range(hidden_size)] for _ in range(input_size)]
		self.weights_hidden_output = [[random.uniform(-1, 1) for _ in range(output_size)] for _ in range(hidden_size)]
		
	def sigmoid(self, x):
		return 1 / (1 + math.exp(-x))
	
	def sigmoid_derivative(self, x):
		return x * (1 - x)
	
	def feedforward(self, inputs):
		# Input to hidden layer
		self.hidden_layer = [0] * self.hidden_size
		for i in range(self.hidden_size):
			for j in range(self.input_size):
				self.hidden_layer[i] += inputs[j] * self.weights_input_hidden[j][i]
			self.hidden_layer[i] = self.sigmoid(self.hidden_layer[i])
		
		# Hidden to output layer
		self.output_layer = [0] * self.output_size
		for i in range(self.output_size):
			for j in range(self.hidden_size):
				self.output_layer[i] += self.hidden_layer[j] * self.weights_hidden_output[j][i]
			self.output_layer[i] = self.sigmoid(self.output_layer[i])
		
		return self.output_layer
	
	def backpropagate(self, inputs, expected_output):
		# Calculate output layer error
		output_errors = [expected_output[i] - self.output_layer[i] for i in range(self.output_size)]
		
		# Calculate hidden layer error
		hidden_errors = [0] * self.hidden_size
		for i in range(self.hidden_size):
			for j in range(self.output_size):
				hidden_errors[i] += output_errors[j] * self.weights_hidden_output[i][j]
		
		# Update weights from hidden to output layer
		for i in range(self.hidden_size):
			for j in range(self.output_size):
				delta = output_errors[j] * self.sigmoid_derivative(self.output_layer[j]) * self.hidden_layer[i]
				self.weights_hidden_output[i][j] += self.learning_rate * delta
		
		# Update weights from input to hidden layer
		for i in range(self.input_size):
			for j in range(self.hidden_size):
				delta = hidden_errors[j] * self.sigmoid_derivative(self.hidden_layer[j]) * inputs[i]
				self.weights_input_hidden[i][j] += self.learning_rate * delta
	def train(self, training_data, epochs):
			for epoch in range(epochs):
				for inputs, expected_output in training_data:
					self.feedforward(inputs)
					self.backpropagate(inputs, expected_output)
	def predict(self, inputs):
			return self.feedforward(inputs)
	def rules(self):
			return {
				"input_size": self.input_size,
				"hidden_size": self.hidden_size,
				"output_size": self.output_size,
				"learning_rate": self.learning_rate
			}
def report_intelegance_level(trainer):
	# Simple heuristic: higher hidden size and more training epochs imply higher intelligence
	intelligence_level = trainer.hidden_size * 10  # Arbitrary scaling factor
	return intelligence_level
def main():
	# Example usage
	trainer = NeuralNetTrainer(input_size=3, hidden_size=5, output_size=2, learning_rate=0.05)
	
	# Dummy training data: (inputs, expected_output)
	training_data = [
		([0, 0, 0], [0, 0]),
		([0, 0, 1], [0, 1]),
		([0, 1, 0], [0, 1]),
		([0, 1, 1], [1, 0]),
		([1, 0, 0], [0, 1]),
		([1, 0, 1], [1, 0]),
		([1, 1, 0], [1, 0]),
		([1, 1, 1], [1, 1]),
	]
	
	trainer.train(training_data, epochs=10000)
	
	# Test prediction
	test_input = [1, 0, 1]
	prediction = trainer.predict(test_input)
	print(f"Prediction for input {test_input}: {prediction}")
	
	# Report intelligence level
	intelligence_level = report_intelegance_level(trainer)
	print(f"Neural Network Intelligence Level: {intelligence_level}")
	
if __name__ == "__main__":
	main()