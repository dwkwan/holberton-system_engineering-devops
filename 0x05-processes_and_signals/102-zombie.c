#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * createzombie - creates a zombie process
 *
 * Return: nothing
 */
void createzombie(void)
{
	pid_t my_pid;

	if (fork() == 0)
	{
		my_pid = getpid();
		printf("Zombie process created, PID: %u\n", my_pid);
		exit(0);
	}
}
/**
 * infinite_while - creates an infinite loop
 *
 * Return: nothing
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
 * main - passes execution control
 *
 * Return: nothing
 */
int main(void)
{
	int i;

	i = 0;
	while (i < 5)
	{
		createzombie();
		i++;
	}
	infinite_while();
	return (0);
}
