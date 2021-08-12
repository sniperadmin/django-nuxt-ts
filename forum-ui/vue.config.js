module.exports = {
  transpileDependencies: ["vuetify"],
  configureWebpack: {
    resolve: {
      mainFields: ["main", "module"],
    },
  },
};
