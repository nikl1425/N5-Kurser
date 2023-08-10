const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");


const inputPath = path.resolve(__dirname, "client/");
const outputPath = path.resolve(__dirname, "client/static/dist");

module.exports = {
  mode: "development",
  entry: path.resolve("./client/index.js"),
  output: {
    path: outputPath,
  },
  plugins: [new MiniCssExtractPlugin({filename: 'output.css'})],
  module: {
    rules: [
      {
        test: /\.css$/i,
        include: inputPath,
        use: [
          "style-loader",
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
                esModule: false,
            }
          },
          {
            loader: "css-loader",
            options: {
              url: false,
            },
          },
          "postcss-loader",
        ],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: [["@babel/preset-env", { targets: "defaults" }]],
            plugins: ["@babel/plugin-proposal-class-properties"],
          },
        },
      },
      {
        test: /\.(eot|svg|ttf|woff|woff2|png|jpg|gif)$/i,
        type: 'asset',
      },
    ],
  },
};
