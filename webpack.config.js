const path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { VueLoaderPlugin } = require('vue-loader');
const CopyPlugin = require("copy-webpack-plugin");

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

    resolve: {
        alias: {
          'vue$': 'vue/dist/vue.esm.js'
        },
        extensions: ['.js', '.jsx', '.scss', '.vue'],

        modules: [
            path.resolve('./src/js/components'),
            path.resolve('node_modules'),
            path.resolve('./src/scss'),
        ]
    },
    plugins: [
        new CleanWebpackPlugin(),
        new VueLoaderPlugin(),
        new HtmlWebpackPlugin({
          title: "Webpack Output",
        }),
         new CopyPlugin({
          patterns: [
            { from: "./src/index.html", to: "test.html" },

          ],
        }),
    ],
     module: {
         rules: [
             {
                 test: /.vue$/,
                 loader: 'vue-loader'
             },


         ]
     }
};


