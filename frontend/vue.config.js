const path = require("path");
module.exports = {
  chainWebpack: (config) => {
    config.plugin("html").tap((args) => {
      args[0].title = "Gestión de mensajeros";
      return args;
    });
    const types = ["vue-modules", "vue", "normal-modules", "normal"];
    types.forEach((type) =>
      addStyleResource(config.module.rule("stylus").oneOf(type))
    );
  },
  configureWebpack: {
    resolve: {
      alias: {
        "@components": path.resolve(__dirname, "./src/components/"),
        "@views": path.resolve(__dirname, "./src/views/"),
        "@scripts": path.resolve(__dirname,"./src/scripts/")
      },
    },
  },
};

function addStyleResource(rule) {
  rule
    .use("style-resource")
    .loader("style-resources-loader")
    .options({
      patterns: [
        path.resolve(__dirname, "./src/styles/vars.styl"),
        path.resolve(__dirname, "./src/styles/mixins.styl"),
      ],
    });
}
