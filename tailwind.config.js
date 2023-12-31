module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin'),
    'prettier-plugin-tailwindcss',
    '@tailwindcss/line-clamp'
  ],
}