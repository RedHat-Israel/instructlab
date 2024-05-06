# Training

You're now at the training phase. So far, you have handcrafted some prompts and
responses, and used `ilab generate` to synthesize those prompt/response pairs
into a new data set.

If you have a Mac Silicon (M1 or newer), we _strongly_ recommend using
`ilab train` locally, and only proceed here if you hit issues.

Also, there is active work being done to support Linux, so if you have
access to a Linux machine with GPUs, that might also be a better option.

Next, you'll get to fine-tune a LoRA (Low-Rank Adaptation of Large Language
Models) using a Jupyter notebook and (preferably) Google Colab platform.

We've laid out the steps to get started with either platform below.

## Setting up the notebook

### Google Colab

Pre-requisites:

* [Google Colab](https://research.google.com/colaboratory/faq.html)
* A Gmail account that you're logged into. This will allow you to use Google Colab, which in the free tier will give you access to an NVidia T4 x 15GB GPU.

**NOTE: At present, you'll need to download the notebook and upload it to Google Colab. To upload a notebook go to [Google Colab](https://colab.research.google.com) and you will be prompted to upload a notebook. Once this repository is open sourced, we will make an 'Open in Colab' button.**

## Running the notebook

[The notebook](./Training_a_LoRA_With_Instruct_Lab.ipynb) in this folder will walk you through:

1. Uploading the output of `ilab generate` (a synthetic dataset created based on your hand written prompts/responses).
1. Checking the base model before training
1. Setting up and training a LoRA. A LoRA uses Parameter Efficient Fine-tuning (PEFT) methods to fine-tune a model on a small subset of the overall parameters, allowing you to conduct fine-tuning in a fraction of the time, on a fraction of the hardware required. The resultant model should be updated and better handle your queries than the base model.
1. Inspecting the output model to make sure the LoRA training had the desired effect (i.e. the output has improved).

Once you have finished training and the output looks good, we encourage you go to stage, [Testing the fine-tuned model](../README.md#-test-the-newly-trained-model)

