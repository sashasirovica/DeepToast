# DeepToast
DeepToast is a deep neural network powered chess engine.

DeepToast is currently being implemented. It will train a neural network to predict Stockfish evaluations of chess positions. The current plan is to train the eval function off the [Lichess training](https://database.lichess.org/) dataset. 

For search functionality I plan to hook up the eval function with the open source [Sunfish engine](https://github.com/thomasahle/sunfish).