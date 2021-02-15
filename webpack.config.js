const path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: {
        main: path.resolve(__dirname, './src/app.js'),
    },
    mode: 'development',
    devtool: 'inline-source-map',
    devServer: {
        publicPath: "/",
        contentBase: "./public",
        hot: true,
        open:true,
    },
    output: {
        filename: '[name].bundle.js',
        publicPath: '/',
        path: path.resolve(__dirname, 'public'),
    },
    watchOptions: {
        ignored: /node_modules/,
        aggregateTimeout: 200,
        poll: 1000
   },
   plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
          title: "Webpack Output",
        })
  ],
};


