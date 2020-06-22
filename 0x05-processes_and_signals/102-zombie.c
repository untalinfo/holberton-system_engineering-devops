#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - infinite loop for zombie process
 * Return: O if success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create a zombie process
 * Return: O if success
 */
int main(void)
{
	int count = 0;
	pid_t zombieP;

	while (count < 5)
	{
		zombieP = fork();
		if (zombieP > 0)
			printf("Zombie process created, PID: %i\n", zombieP);
		else
			exit(0);
		count++;
	}
	infinite_while();
	return (0);
}
