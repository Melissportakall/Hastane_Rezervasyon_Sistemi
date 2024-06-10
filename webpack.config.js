const path = require('path');

module.exports = {
  entry: './src/index.js', // Ana giriş noktası
  output: {
    filename: 'bundle.js', // Çıktı dosyasının adı
    path: path.resolve(__dirname, 'dist') // Çıktı dosyasının konumu
  }
};
