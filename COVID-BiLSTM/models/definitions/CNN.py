
import torch
import torch.nn as nn


Tensor = torch.Tensor


class CNN(nn.Module):
    
    def __init__(self, filters_per_layer: list[int, ...], kernel_size=3, bias=False):
        super().__init__()

        layers = []

        for d_in, d_out in zip(filters_per_layer[:-1], filters_per_layer[1:]):

            # expose the model params for future tuning
            layer = nn.Conv1d(in_channels=d_in,
                              out_channels=d_out,
                              kernel_size=kernel_size,
                              bias=bias,
                              stride=1,
                              padding=0)
            layers.append(layer)
            layers.append(nn.BatchNorm1d(num_features=d_out,
                                         affine=True))  # learnable params
            layers.append(nn.ReLU())

        # add final average pooling and dense layer
        layers.append(nn.AdaptiveAvgPool2d((1, 64)))
        layers.append(nn.Linear(in_features=64, out_features=1))
        layers.append(nn.ReLU())

        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model(x)

