module.exports = {
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
		theme: {
			minHeight: {
				'0': '0',
				'1/4': '25%',
				'1/2': '50%',
				'3/4': '75%',
				'full': '100%',
			},
			minWidth: {
				'0': '0',
				'1/4': '25%',
				'1/2': '50%',
				'3/4': '75%',
				'full': '100%',
			},
			maxHeight: {
						'0': '0',
						'1/4': '25%',
						'1/2': '50%',
						'3/4': '75%',
						'full': '100%',
					},
			maxWidth: {
						'0': '0',
						'1/4': '25%',
						'1/2': '50%',
						'3/4': '75%',
						'full': '100%',
					},
    purge: {
        enabled: false, //true for production build
        content: [
            '../**/templates/*.html',
            '../**/templates/**/*.html'
        ]
    },
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [],
}
