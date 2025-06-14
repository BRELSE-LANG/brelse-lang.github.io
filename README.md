// File: README.md

BrelseLang Landing Page

A sleek, tech-forward landing page for BrelseLang — the world's first hybrid language blending Braille and Morse code.

Features

Dark theme UI

Tailwind CSS styling

Futuristic branding

Sections: Hero, About, Features, Call to Action


Tech Stack

React.js

Tailwind CSS

GitHub Pages (deployment)



---

// File: index.html

<!DOCTYPE html><html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>BrelseLang</title>
    <link href="/dist/output.css" rel="stylesheet">
  </head>
  <body class="bg-black text-white">
    <div id="root"></div>
  </body>
</html>
---

// File: src/App.jsx import React from 'react'; import Hero from './components/Hero'; import About from './components/About'; import Features from './components/Features'; import CTA from './components/CTA';

function App() { return ( <div className="font-sans"> <Hero /> <About /> <Features /> <CTA /> </div> ); }

export default App;


---

// File: src/components/Hero.jsx import React from 'react';

const Hero = () => (

  <section className="h-screen flex flex-col justify-center items-center text-center px-4">
    <h1 className="text-5xl md:text-7xl font-bold mb-4">BrelseLang</h1>
    <p className="text-xl md:text-2xl mb-6">From Dots to Data — The Future is Tactile</p>
    <a href="#about" className="bg-blue-600 hover:bg-blue-700 text-white py-3 px-6 rounded-full">Learn More</a>
  </section>
);export default Hero;


---

// File: src/components/About.jsx import React from 'react';

const About = () => (

  <section id="about" className="py-20 px-6 text-center">
    <h2 className="text-4xl font-bold mb-4">What is BrelseLang?</h2>
    <p className="max-w-2xl mx-auto">
      BrelseLang is a revolutionary language system that fuses Braille and Morse code into a unified programming interface. Designed to make communication more inclusive, encrypted, and adaptive — especially in defense and accessibility technologies.
    </p>
  </section>
);export default About;


---

// File: src/components/Features.jsx import React from 'react';

const features = [ 'Tactile communication system', 'Hybrid Braille-Morse syntax', 'MVP-ready prototypes', 'Military-grade encrypted signaling', ];

const Features = () => (

  <section className="py-20 px-6 bg-gray-900 text-center">
    <h2 className="text-4xl font-bold mb-10">Key Features</h2>
    <ul className="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
      {features.map((f, idx) => (
        <li key={idx} className="bg-gray-800 p-6 rounded-xl text-lg">{f}</li>
      ))}
    </ul>
  </section>
);export default Features;


---

// File: src/components/CTA.jsx import React from 'react';

const CTA = () => (

  <section className="py-20 px-6 text-center">
    <h2 className="text-3xl font-bold mb-4">Ready to Collaborate or Fund?</h2>
    <p className="mb-6">Join us in shaping the future of secure, inclusive communication.</p>
    <a href="mailto:founder@brelselang.org" className="bg-green-600 hover:bg-green-700 text-white py-3 px-6 rounded-full">Contact Us</a>
  </section>
);export default CTA;


---

// File: tailwind.config.js module.exports = { content: ['./index.html', './src/**/*.{js,jsx}'], theme: { extend: {}, }, plugins: [], };


---

// File: package.json { "name": "brelselang-landing", "version": "1.0.0", "private": true, "scripts": { "dev": "vite", "build": "vite build", "preview": "vite preview" }, "dependencies": { "react": "^18.2.0", "react-dom": "^18.2.0" }, "devDependencies": { "vite": "^5.0.0", "tailwindcss": "^3.3.0", "autoprefixer": "^10.4.0", "postcss": "^8.4.0" } }


---

// File: postcss.config.js module.exports = { plugins: { tailwindcss: {}, autoprefixer: {}, }, };

# BrelseLang-landing-page
