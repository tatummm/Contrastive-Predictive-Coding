import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

device=torch.device("cuda" if torch.cuda.is_available() else "cpu")

input_size=1024
hidden_size=1024
code_size=1024
batch_size=1

class Autoregressive_RNN:
	def __init__(self,num_layers=1,batch_size=batch_size):
		super(Autoregressive, self).__init()
			self.hidden_size=hidden_size
			self.batch_size=batch_size
			self.num_layers=num_layers
			self.rnn=nn.GRU(input_size,hidden_size,num_layers=self.num_layers)
			self.linear=nn.Linear(hidden_size,code_size)

	def forward(self,X):
		return self.generate(self.autoregress(X))

	def autoregress(self,X):
		hidden=init_hidden()
		output,hidden=self.rnn(X,hidden)
		return hidden

	def generate(self,X):
		return self.linear(X)

	def init_hidden(self):
		return torch.zeros(self.num_layers,self.batch_size,self.hidden_size,device=device)