(defun isOddorEven (x)
 (if (= 0 (% x 2 ))
		  (format "%d is Even." x)
	  (format "%d is Odd." x)))

(isOddorEven 4)
