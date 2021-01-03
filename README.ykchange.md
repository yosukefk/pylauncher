## Change in this fork
### Intension
I wanted to provide IbrunLauncher to acknowledge dependencies.  For example, i wold heve command list file like below:

<pre>
4,  , ./exec parametersA day1
4, 0, ./exec parametersA day2
4, 1, ./exec parametersA day3
4,  , ./exec parametersB day1
4, 3, ./exec parametersB day2
4, 4, ./exec parametersB day3
4,  , ./exec parametersC day1
4, 6, ./exec parametersC day2
4, 7, ./exec parametersC day3
</pre>

I want to run same executable ./exe with three different prameter sets (A , B and C, somehow specified as arguments).  But I need to run the code three time for three days to be simulated, as day2 simulation is dependent of results of day1 simulatons.

The example uses 4 cores for each task (first field), and secnod field shows dependencies fields, telling that second task is dependend on first task.

### What was done
* Modified `Commandline` class to be like and observer pattern, registering itself to depedent Commandline object.  
* `Task` class holds on to `Commandline` object, and upon completion it notifies subscribers which are depnding other `Commandline` object, to clear the flag.  
* `CommandlineGenerator` does not yield Commandline whose dependency is not cleared, and yield "stall" instead if there is nothing to provide
