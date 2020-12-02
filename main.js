const intro = introJs();

intro.setOption({
    steps: [
        {
            intro: 'Welcome to our new website'
        },
        {
            element: '#step-one',
            inro: 'Please read this! It is important.'
        }
    ]
})

intro.start();