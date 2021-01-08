const webpack = require('webpack')
const path = require('path')
const BundleTracker = require('webpack-bundle-tracker')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

const inProduction = 'production' === process.env.NODE_ENV
const buildPath = path.resolve(__dirname, 'build/')

module.exports = {
  entry: {
    styles: './scss/styles.scss',
    scrollToTop: './js/scrollToTop.js',
    //vendor: [],
  },

  devtool: inProduction ? 'source-map' : 'eval-source-map',

  output: {
    path: buildPath,
    filename: './bundles/[name]-[hash].js',
    publicPath: '',
  },

  plugins: [
    //new webpack.optimize.CommonsChunkPlugin({name: 'vendor'}),
    new CleanWebpackPlugin({
      cleanStaleWebpackAssets: false,
    }),
    new BundleTracker({
      filename: './webpack-stats.json',
    }),
    new MiniCssExtractPlugin({
      filename: './bundles/[name]-[hash].css',
    }),
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: [/node_modules/],
        use: [{
          loader: 'babel-loader',
        }],
      },
      {
        test: /\.scss$/,
        exclude: [/node_modules/],
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              sourceMap: true,
            }
          },
          {
            loader: 'sass-loader',
            options: {
              sourceMap: true,
              sassOptions: {
                outputStyle: 'compressed',
              },
            },
          }
        ],
      },
    ],
  },
}
