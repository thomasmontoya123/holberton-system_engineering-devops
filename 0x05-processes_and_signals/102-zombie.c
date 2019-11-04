#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>

/**
 * infinite_while - loop
 *
 * Return: void
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
 * main - entry point
 *
 * Return: always 0 (success)
 */

int main(void)
{
	unsigned int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie == 0)
			exit(EXIT_FAILURE);
		else
			printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (0);
}
