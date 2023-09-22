# Fine-tuning

### Pre-trained model
|      Model       | Image Size | Data Augmentation | Dense Layer | Dropout Rate | Parameters | Accuracy |
| :--------------: | :--------: | :---------------: | :---------: | :----------: | :--------: | :------: |
|     ResNet50     | 300 x 300  |        Low        |    None     |     0.2      |   23.6M    |  75.0%   |
|    ResNet50V2    | 300 x 300  |        Low        |    None     |     0.2      |   23.6M    |  74.1%   |
| EfficientNetV2B0 | 300 x 300  |        Low        |    None     |     0.2      |    6.0M    |  79.6%   |
| EfficientNetV2S  | 300 x 300  |        Low        |    None     |     0.2      |   20.4M    |  79.7%   |
| EfficientNetV2M  | 300 x 300  |        Low        |    None     |     0.2      |   53.2M    |  80.4%   |

Best results were obtained with the EfficientNet models. EfficientNetV2B0 and EfficientNetV2S will be favored because of their lighter dimensions.