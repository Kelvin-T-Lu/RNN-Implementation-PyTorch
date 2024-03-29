import torch
import torch.nn as nn


class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, model_type="rnn", n_layers=1):
        super(RNN, self).__init__()
        """
        Initialize the RNN model.
        
        You should create:
        - An Embedding object which will learn a mapping from tensors
        of dimension input_size to embedding of dimension hidden_size.
        - Your RNN network which takes the embedding as input (use models
        in torch.nn). This network should have input size hidden_size and
        output size hidden_size.
        - A linear layer of dimension hidden_size x output_size which
        will predict output scores.

        Inputs:
        - input_size: Dimension of individual element in input sequence to model
        - hidden_size: Hidden layer dimension of RNN model
        - output_size: Dimension of individual element in output sequence from model
        - model_type: RNN network type can be "rnn" (for basic rnn), "gru", or "lstm"
        - n_layers: number of layers in your RNN network
        """
        
        self.model_type = model_type
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_layers = n_layers
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        self.embedding  = torch.nn.Embedding(self.input_size, self.hidden_size)
        self.rnn = torch.nn.RNN(self.input_size, self.hidden_size, self.n_layers)
        self.gru = torch.nn.GRU(self.input_size, self.hidden_size, self.n_layers)
        self.lstm = torch.nn.LSTM(self.input_size, self.hidden_size, self.n_layers)
        self.linear = torch.nn.Linear(hidden_size, output_size)
        
        ##########       END      ##########
        


    def forward(self, input, hidden):
        """
        Forward pass through RNN model. Use your Embedding object to create 
        an embedded input to your RNN network. You should then use the 
        linear layer to get an output of self.output_size. 

        Inputs:
        - input: the input data tensor to your model of dimension (batch_size)
        - hidden: the hidden state tensor of dimension (n_layers x batch_size x hidden_size) 

        Returns:
        - output: the output of your linear layer
        - hidden: the output of the RNN network before your linear layer (hidden state)
        """
        
        output = None
        hidden = None
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        x = self.embedding(input)
        x = x.view(1, input.size(0), -1)
        if self.model_type == "rnn":
          output, hidden = self.rnn(x, hidden)
        elif self.model_type == "gru":
          output, hidden = self.gru(x, hidden)
        elif self.model_type == "lstm":
          output, hidden = self.lstm(x, hidden)
        ##########       END      ##########
        
        output = output.reshape(input.size(0), -1)
        output = self.linear(output)
        
        ##########       END      ##########
        
        
        return output, hidden

    def init_hidden(self, batch_size, device=None):
        """
        Initialize hidden states to all 0s during training.
        
        Hidden states should be initilized to dimension (n_layers x batch_size x hidden_size) 

        Inputs:
        - batch_size: batch size

        Returns:
        - hidden: initialized hidden values for input to forward function
        """
        
        hidden = None
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        hidden = torch.zeros(self.n_layers, batch_size, self.hidden_size)
        hidden = hidden.to(device)

        if self.model_type == "lstm": 
            return (hidden, hidden)
        ##########       END      ##########

        return hidden

