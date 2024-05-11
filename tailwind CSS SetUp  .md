## [tailwind CSS SetUp](https://tailwindcss.com/docs/installation/using-postcss)

        npm init
        
        npm -y
        
        npm install -D tailwindcss postcss autoprefixer vite
        
        npx tailwindcss init -p
          
        npm run start



  tailwind.config.js
  
        /** @type {import('tailwindcss').Config} */
        module.exports = {
          content: ['*'],
          theme: {
            extend: {},
          },
          plugins: [],
        }


  Create folder css -> mina.css
  
        @tailwind base;
        @tailwind components;
        @tailwind utilities;



  package.json
  
  ![image](https://github.com/Md-Merazul-Islam/Django/assets/129538030/38bb429d-7de8-4310-8f73-adc03eca443f)

  html link 

       <link rel="stylesheet" href="css/main.css">


  
