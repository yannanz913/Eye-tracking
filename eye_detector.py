




main()

	Step 1:
		Set up the GUI window with the initial parameter values (by calling your MainWindow class)
			(when OK is clicked, set a global variable called "clicked" to 1
		Initially, set "clicked" to 1
	Step 2:
		Primary loop:
			in a while loop that never ends,
				first check to see if "clicked" is 1
					if it is, then re-make the detectors with the parameters from the window
					set clicked to 0
				second, 
					apply the detector to the image
					(write the results to disk)

