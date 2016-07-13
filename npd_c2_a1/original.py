st login: Mon Jul 11 13:00:45 on ttys002
172-30-49-113:~ adrianmucha$ cd vagrant-python-env
-bash: cd: vagrant-python-env: No such file or directory
172-30-49-113:~ adrianmucha$ ls
Applications				README.md
Applications (original)			Vagrantfile
Creative Cloud Files			VirtualBox VMs
Creative Cloud Files (archived) (1)	directory
Desktop					directory_contents.txt
Documents				get_pizza
Downloads				intro-programming
Library					node_modules
Movies					scripts
Music					untitled folder
Pictures				vagrant-workspace
Public					vagrant_folder
172-30-49-113:~ adrianmucha$ cd Va
-bash: cd: Va: No such file or directory
172-30-49-113:~ adrianmucha$ cd Vagrantfile 
-bash: cd: Vagrantfile: Not a directory
172-30-49-113:~ adrianmucha$ ls
Applications				README.md
Applications (original)			Vagrantfile
Creative Cloud Files			VirtualBox VMs
Creative Cloud Files (archived) (1)	directory
Desktop					directory_contents.txt
Documents				get_pizza
Downloads				intro-programming
Library					node_modules
Movies					scripts
Music					untitled folder
Pictures				vagrant-workspace
Public					vagrant_folder
172-30-49-113:~ adrianmucha$ cd Vagrantfile 
-bash: cd: Vagrantfile: Not a directory
172-30-49-113:~ adrianmucha$ cd intro-programming/
172-30-49-113:intro-programming adrianmucha$ ls
172-30-49-113:intro-programming adrianmucha$ ls
172-30-49-113:intro-programming adrianmucha$ cd ..
172-30-49-113:~ adrianmucha$ ls
Applications				README.md
Applications (original)			Vagrantfile
Creative Cloud Files			VirtualBox VMs
Creative Cloud Files (archived) (1)	directory
Desktop					directory_contents.txt
Documents				get_pizza
Downloads				intro-programming
Library					node_modules
Movies					scripts
Music					untitled folder
Pictures				vagrant-workspace
Public					vagrant_folder
172-30-49-113:~ adrianmucha$ cd vagrant-workspace/
172-30-49-113:vagrant-workspace adrianmucha$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Checking if box 'hashicorp/precise64' is up to date...
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: flag to force provisioning. Provisioners marked to run always will still run.
172-30-49-113:vagrant-workspace adrianmucha$ vagrant ssh
Welcome to Ubuntu 12.04 LTS (GNU/Linux 3.2.0-23-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
New release '14.04.4 LTS' available.
Run 'do-release-upgrade' to upgrade to it.

Welcome to your Vagrant-built virtual machine.
Last login: Mon Jul 11 17:01:18 2016 from 10.0.2.2
vagrant@precise64:~$ ls 
course_setup.sh    npd             Python-3.4.1.tar.xz
course_vars.cfg    postinstall.sh  task_database_python.txt
intro-programming  python          vagrant-python-env
my_stuff           Python-3.4.1    vagrant-python-env1
vagrant@precise64:~$ cd my_stuff/
vagrant@precise64:~/my_stuff$ virtualenv -p python3.4 venv
The program 'virtualenv' is currently not installed.  You can install it by typing:
sudo apt-get install python-virtualenv
vagrant@precise64:~/my_stuff$ ls    
game
vagrant@precise64:~/my_stuff$ cd ..
vagrant@precise64:~$ ls
course_setup.sh    npd             Python-3.4.1.tar.xz
course_vars.cfg    postinstall.sh  task_database_python.txt
intro-programming  python          vagrant-python-env
my_stuff           Python-3.4.1    vagrant-python-env1
vagrant@precise64:~$ mkdir python_exercise
vagrant@precise64:~$ ls
course_setup.sh    postinstall.sh       task_database_python.txt
course_vars.cfg    python               vagrant-python-env
intro-programming  Python-3.4.1         vagrant-python-env1
my_stuff           Python-3.4.1.tar.xz
npd                python_exercise
vagrant@precise64:~$ cd python_exercise/
vagrant@precise64:~/python_exercise$ sudo apt-get install python-virtualenv
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  python-pip python-setuptools
The following NEW packages will be installed:
  python-pip python-setuptools python-virtualenv
0 upgraded, 3 newly installed, 0 to remove and 185 not upgraded.
Need to get 2,648 kB of archives.
After this operation, 3,779 kB of additional disk space will be used.
Do you want to continue [Y/n]? Y
Get:1 http://us.archive.ubuntu.com/ubuntu/ precise/main python-setuptools all 0.6.24-1ubuntu1 [441 kB]
Get:2 http://us.archive.ubuntu.com/ubuntu/ precise/universe python-pip all 1.0-1build1 [95.1 kB]
Get:3 http://us.archive.ubuntu.com/ubuntu/ precise/universe python-virtualenv all 1.7.1.2-1 [2,112 kB]
Fetched 2,648 kB in 2s (896 kB/s)              
Selecting previously unselected package python-setuptools.
(Reading database ... 53608 files and directories currently installed.)
Unpacking python-setuptools (from .../python-setuptools_0.6.24-1ubuntu1_all.deb) ...
Selecting previously unselected package python-pip.
Unpacking python-pip (from .../python-pip_1.0-1build1_all.deb) ...
Selecting previously unselected package python-virtualenv.
Unpacking python-virtualenv (from .../python-virtualenv_1.7.1.2-1_all.deb) ...
Processing triggers for man-db ...
Setting up python-setuptools (0.6.24-1ubuntu1) ...
Setting up python-pip (1.0-1build1) ...
Setting up python-virtualenv (1.7.1.2-1) ...
vagrant@precise64:~/python_exercise$ virtualenv -p python3.4 venv
Running virtualenv with interpreter /usr/local/bin/python3.4
New python executable in venv/bin/python3.4
Also creating executable in venv/bin/python
Failed to import the site module
Traceback (most recent call last):
  File "/home/vagrant/python_exercise/venv/lib/python3.4/site.py", line 67, in <module>
    import os
  File "/home/vagrant/python_exercise/venv/lib/python3.4/os.py", line 614, in <module>
    from _collections_abc import MutableMapping
ImportError: No module named '_collections_abc'
ERROR: The executable venv/bin/python3.4 is not functioning
ERROR: It thinks sys.prefix is '/home/vagrant/python_exercise' (should be '/home/vagrant/python_exercise/venv')
ERROR: virtualenv is not compatible with this system or executable
vagrant@precise64:~/python_exercise$ virtualenv -p python3.4 venv
Running virtualenv with interpreter /usr/local/bin/python3.4
Overwriting venv/lib/python3.4/site.py with new content
Overwriting venv/lib/python3.4/orig-prefix.txt with new content
Overwriting venv/lib/python3.4/no-global-site-packages.txt with new content
New python executable in venv/bin/python3.4
Not overwriting existing python script venv/bin/python (you must use venv/bin/python3.4)
Failed to import the site module
Traceback (most recent call last):
  File "/home/vagrant/python_exercise/venv/lib/python3.4/site.py", line 67, in <module>
    import os
  File "/home/vagrant/python_exercise/venv/lib/python3.4/os.py", line 614, in <module>
    from _collections_abc import MutableMapping
ImportError: No module named '_collections_abc'
ERROR: The executable venv/bin/python3.4 is not functioning
ERROR: It thinks sys.prefix is '/home/vagrant/python_exercise' (should be '/home/vagrant/python_exercise/venv')
ERROR: virtualenv is not compatible with this system or executable
vagrant@precise64:~/python_exercise$ python3 venv
/usr/local/bin/python3: can't find '__main__' module in 'venv'
vagrant@precise64:~/python_exercise$ python
Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
KeyboardInterrupt
>>> :q  
  File "<stdin>", line 1
    :q
    ^
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> 
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> 
vagrant@precise64:~/python_exercise$ bpython
>>> def square(n):
...     '''Square a number n'''
...     return n**2
...     
... def get_first_100():
  File "<input>", line 5
    def get_first_100():
      ^
SyntaxError: invalid syntax
>>> 
vagrant@precise64:~/python_exercise$ touch python_exercise.py
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ python python_exercise.py 
  File "python_exercise.py", line 11
    return_value = []
                    ^
IndentationError: unindent does not match any outer indentation level
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ python python_exercise.py 
Traceback (most recent call last):
  File "python_exercise.py", line 23, in <module>
    print(solve_probblem())
NameError: name 'solve_probblem' is not defined
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ python python_exercise.py 
Traceback (most recent call last):
  File "python_exercise.py", line 23, in <module>
    print(solve_problem())
  File "python_exercise.py", line 18, in solve_problem
    sum_squares_first_hundred = sum(square_list(first_100))
NameError: global name 'square_list' is not defined
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ python python_exercise.py 
Traceback (most recent call last):
  File "python_exercise.py", line 23, in <module>
    print(solve_problem())
  File "python_exercise.py", line 18, in solve_problem
    sum_squares_first_hundred = sum(square_list(first_100))
NameError: global name 'square_list' is not defined
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ python python_exercise.py 
Traceback (most recent call last):
  File "python_exercise.py", line 23, in <module>
    print(solve_problem())
  File "python_exercise.py", line 18, in solve_problem
    sum_squares_first_hundred = sum(square_list(first_100))
NameError: global name 'square_list' is not defined
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ python python_exercise.py 
Traceback (most recent call last):
  File "python_exercise.py", line 23, in <module>
    print(solve_problem())
  File "python_exercise.py", line 18, in solve_problem
    sum_squares_first_hundred = sum(square_list(first_100))
  File "python_exercise.py", line 13, in square_list
    return_value.append(square(number))
NameError: global name 'square' is not defined
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ python python_exercise.py 
Traceback (most recent call last):
  File "python_exercise.py", line 23, in <module>
    print(solve_problem())
  File "python_exercise.py", line 20, in solve_problem
    return sum_sqares_first_hundred - square_sum_first_hundred
NameError: global name 'sum_sqares_first_hundred' is not defined
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ python python_exercise.py 
Traceback (most recent call last):
  File "python_exercise.py", line 23, in <module>
    print(solve_problem())
  File "python_exercise.py", line 20, in solve_problem
    return sum_sqares_first_hundred - square_sum_first_hundred
NameError: global name 'sum_sqares_first_hundred' is not defined
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ python python_exercise.py 
-25502499
vagrant@precise64:~/python_exercise$ ls
python_exercise.py  venv
vagrant@precise64:~/python_exercise$  git clone https://github.com/adrianomucha/npd_c2_a1.git
Cloning into 'npd_c2_a1'...
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
vagrant@precise64:~/python_exercise$ ls
npd_c2_a1  python_exercise.py  venv
vagrant@precise64:~/python_exercise$ cd npd_c2_a1/
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
vagrant@precise64:~/python_exercise/npd_c2_a1$ git status 
# On branch master
nothing to commit (working directory clean)
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
vagrant@precise64:~/python_exercise/npd_c2_a1$ cd ..
vagrant@precise64:~/python_exercise$ ls
npd_c2_a1  python_exercise.py  venv
vagrant@precise64:~/python_exercise$ cd npd_c2_a1/
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
vagrant@precise64:~/python_exercise/npd_c2_a1$ touch original.py
vagrant@precise64:~/python_exercise/npd_c2_a1$ touch refactored.py
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
original.py  refactored.py
vagrant@precise64:~/python_exercise/npd_c2_a1$ vim original.py 
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
original.py  refactored.py
vagrant@precise64:~/python_exercise/npd_c2_a1$ cd ..
vagrant@precise64:~/python_exercise$ ls
npd_c2_a1  python_exercise.py  venv
vagrant@precise64:~/python_exercise$ ;s
-bash: syntax error near unexpected token `;'
vagrant@precise64:~/python_exercise$ ls
npd_c2_a1  python_exercise.py  venv
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ cd npd_c2_a1/
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
original.py  refactored.py
vagrant@precise64:~/python_exercise/npd_c2_a1$ vim refactored.py 
vagrant@precise64:~/python_exercise/npd_c2_a1$ vim original.py 
vagrant@precise64:~/python_exercise/npd_c2_a1$ cd ..                
vagrant@precise64:~/python_exercise$ ls
npd_c2_a1  python_exercise.py  venv
vagrant@precise64:~/python_exercise$ python python_exercise.py 
-25502499
vagrant@precise64:~/python_exercise$ vim python_exercise.py 
vagrant@precise64:~/python_exercise$ ls  
npd_c2_a1  python_exercise.py  venv
vagrant@precise64:~/python_exercise$ cd npd_c2_a1/
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
original.py  refactored.py
vagrant@precise64:~/python_exercise/npd_c2_a1$ vim original.py 
vagrant@precise64:~/python_exercise/npd_c2_a1$ python original.py 
  File "original.py", line 17
    return return_value = []
                        ^
SyntaxError: invalid syntax
vagrant@precise64:~/python_exercise/npd_c2_a1$ vim original.py 
vagrant@precise64:~/python_exercise/npd_c2_a1$ python original.py 
  File "original.py", line 19
    for number in first_fifty:
    ^
IndentationError: unexpected indent
vagrant@precise64:~/python_exercise/npd_c2_a1$ vim original.py 
vagrant@precise64:~/python_exercise/npd_c2_a1$ python original.py 
  File "original.py", line 17
    return return_value = []
                        ^
SyntaxError: invalid syntax
vagrant@precise64:~/python_exercise/npd_c2_a1$ vim original.py 
vagrant@precise64:~/python_exercise/npd_c2_a1$ python original.py 
  File "original.py", line 19
    return return_value
SyntaxError: 'return' outside function
vagrant@precise64:~/python_exercise/npd_c2_a1$ vim original.py 
vagrant@precise64:~/python_exercise/npd_c2_a1$ python original.py 
  File "original.py", line 17
    for number in first_fifty:
      ^
IndentationError: expected an indented block
vagrant@precise64:~/python_exercise/npd_c2_a1$ vim original.py 
vagrant@precise64:~/python_exercise/npd_c2_a1$ python original.py 
  File "original.py", line 18
    if number % 2 == 0:
     ^
IndentationError: expected an indented block
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls  
original.py  refactored.py
vagrant@precise64:~/python_exercise/npd_c2_a1$ cd ..
vagrant@precise64:~/python_exercise$ ls
npd_c2_a1  python_exercise.py  venv
vagrant@precise64:~/python_exercise$ git add npd_c2_a1/
fatal: Not a git repository (or any of the parent directories): .git
vagrant@precise64:~/python_exercise$ git init
Initialized empty Git repository in /home/vagrant/python_exercise/.git/
vagrant@precise64:~/python_exercise$ git add npd_c2_a1/
vagrant@precise64:~/python_exercise$ git commit -m"for later"
[master (root-commit) 854e7fd] for later
 2 files changed, 120 insertions(+)
 create mode 100644 npd_c2_a1/.gitignore
 create mode 100644 npd_c2_a1/original.py
 create mode 100644 npd_c2_a1/refactored.py
vagrant@precise64:~/python_exercise$ git push
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>

vagrant@precise64:~/python_exercise$ git push -u origin master
fatal: 'origin' does not appear to be a git repository
fatal: The remote end hung up unexpectedly
vagrant@precise64:~/python_exercise$ ls
npd_c2_a1  python_exercise.py  venv
vagrant@precise64:~/python_exercise$ cd npd_c2_a1/
vagrant@precise64:~/python_exercise/npd_c2_a1$ ls
original.py  refactored.py
vagrant@precise64:~/python_exercise/npd_c2_a1$ vim original.py 

  1 e range of numbers 1 to 50                                                                          
  2 # sum even integers                                                                                 
  3 # define the sum of numbers which are divisble by 7                                                 
  4 # print                                                                                             
  5                                                                                                     
  6 def first_fifty():                                                                                  
  7     return list(range(1,51))                                                                        
  8                                                                                                     
  9 print(first_fifty())                                                                                
 10                                                                                                     
 11 def return_value():                                                                                 
 12     for number in first_fifty:                                                                      
 13     if number % 2 == 0:                                                                             
 14     return_value.append(number)                                                                     
 15     return return_value                                                                             
 16                                                                                                     
 17 def solve_problem():                                                                                
 18     first_50 = first_fifty()                                                                        
 19     sum_first_50 = sum(even_numbers(first_50))                                                      
 20                                                                                                     
 21                                                                                                     
 22                                                                                                     
 23                                                                                                     
 24                                                                                                     
 25                                                                                                     
 26                                                                                                     
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
~                                                                                                                                                                                 
original.py [+]                                                                                                                                                 1,8            All
23 fewer lines; before #3  2 seconds ago

