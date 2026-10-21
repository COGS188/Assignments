# Instructions

Please see bandits.ipynb for a step by step guide on how to complete this assignment.

Please submit **slot_machine.py**, and **bandits.py**, to gradescope. Ensure the filenames are left as-is, any other filename will fail the autograder. 

You do not need to submit bandits.ipynb to gradescope.

-----

## Creating a Conda Environment from `environment.yml`

To create a Conda environment using an `environment.yml` file located in the current directory, follow these steps:

## Prerequisites
- Ensure you have [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/) installed on your system.
- Open a terminal (Linux/macOS) or Anaconda Prompt (Windows).

## Steps

1. Navigate to the Directory (Optional)

If your `environment.yml` is not in the current directory, navigate to the correct location using:

cd /path/to/directory

2. Create the Conda Environment

Run the following command:

```bash
conda env create -f environment.yml
```

This will create a new Conda environment with the dependencies specified in environment.yml.

3. Activate the Environment

Once the environment is created, activate it using:

```bash
conda activate <env_name>
```

Replace `<env_name>` with the name of the environment specified in environment.yml.

4. Verify Installation

Check if the environment is successfully installed by running:

```bash
conda env list
```

or

```bash
conda info --envs
```

Your newly created environment should be listed.

