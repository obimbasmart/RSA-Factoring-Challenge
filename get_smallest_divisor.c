#include "main.h"

/**
 * smallest_divisor - returns the smallest divisor of a number
 * @n: integer
 *
 * Return: integer
 */
long int smallest_divisor(long int n)
{
	long int temp;

	if (n % 2 == 0)
		return 2;

	temp = 3;	
	while (temp * temp <= n)
	{
		if (n % temp == 0)
			return temp;
		else
			temp += 2;
	}
	/* prime number */
	return (1);
}



















