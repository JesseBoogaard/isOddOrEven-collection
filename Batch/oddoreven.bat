set /a a = %num% %% 2
if %a% == 0 (
	echo This is even
) else (
	echo This is odd
)