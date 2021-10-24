class VGG(nn.Module):

    def __init__(self, global_params=None):
        """ An VGGNet model that predicts the class of an image based on food type
        Args:
          global_params (namedtuple): A set of GlobalParams shared between blocks
        Examples:
          model = VGG.from_pretrained('vgg11')
            """
            super(VGG, self).__init__()
            self.features = nn.Sequential(
                # Conv1
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # Conv2
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # Conv3
            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),

            nn.MaxPool2d(kernel_size=2, stride=2),
            # Conv4
            nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            def extract_features(self, x):
              x = self.features(x) # x: [b, 512, h, w]
              return x

            def forward(self, x):
              x = self.features(x) # x: [b, 512, h, w]
              x = x.view(x.size(0), -1) # x: [b, 512*h*w]
              x = self.classifier(x) # x: [b, 1000]
              return x

            @classmethod
            def from_name(cls, model_name, **kwargs):
              # Load weights from a PyTorch model
              model_urls = { 
                'vgg11': 'https://download.pytorch.org/models/vgg11-bbd30ac9.pth',
                'vgg13': 'https://download.pytorch.org/models/vgg13-c768596a.pth',
                'vgg16': 'https://download.pytorch.org/models/vgg16-397923af.pth',
                'vgg19': 'https://download.pytorch.org/models/vgg19-dcbb9e9d.pth',
                'vgg11_bn': 'https://download.pytorch.org/models/vgg11_bn-6002323d.pth',
                'vgg13_bn': 'https://download.pytorch.org/models/vgg13_bn-abd245e5.pth',
                'vgg16_bn': 'https://download.pytorch.org/models/vgg16_bn-6c64b313.pth',
                'vgg19_bn': 'https://download.pytorch.org/models/vgg19_bn-c79401a0.pth',
              }
              model = cls(**kwargs) # model: VGG(**kwargs)
              state_dict = load_state_dict_from_url(model_urls[model_name],
                                                    progress=progress)    
              model.load_state_dict(state_dict)
            
            def make_layers(self, cfg, batch_norm=False):
              layers = []
              in_channels = 3
              for v in cfg:
                if v == 'M':
                  layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
                else:
                  conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)
                  if batch_norm:
                    layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
                  else:
                    layers += [conv2d, nn.ReLU(inplace=True)]
                  in_channels = v
              return nn.Sequential(*layers)