# DeepToast
DeepToast is a deep neural network powered chess engine. The name comes from my cat Toasty pictured below. If the engine can beat him I'll be happy!
![toasty_zarra](https://user-images.githubusercontent.com/5005269/113540793-bb4d4080-9595-11eb-8bec-22dcae202bff.jpg)

DeepToast is currently being implemented. It will train a neural network to predict Stockfish evaluations of chess positions. The current plan is to train the eval function off the [Lichess training](https://database.lichess.org/) dataset. 

For search functionality I plan to hook up the eval function with the open source [Sunfish engine](https://github.com/thomasahle/sunfish).
