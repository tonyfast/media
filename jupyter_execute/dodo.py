#!/usr/bin/env python
# coding: utf-8

# In[6]:


from pathlib import Path


# # `qshop` for configuration and builds
# 
# in open source software, there are conventions, like git and github, that provide important project metadata. for blogs and documentation, this information is transcribed by hand for one off documentation builds. `qshop` simplifies bootstrapping blog and documentation for projects by aggregating project metadata and providing best practices for starting your docuemntation.
# 
# `qshop` provides:
# 
# * centralized models for common configurations
#     * these models export json schema, and create a common pool for schema configuration
# * command line and ipython magic usage
#     * the qshop tasks are automatically loaded for use with the existing `doit` magic
# * extensible tasks for doing more with `qshop`
# 
#     a lot of schema for common tools are undefined or works in progress. having a common sink for these configurations will help provide schema to facilitate in configuration.

# ## how does it help
# 
# `qshop` provides strong opinions for properly building documentation with tools like nikola and sphinx.

# ## how to use it
# 
# `qshop` requires a github project to exist to build your documentation. it configures your docuemntation using the git and github api's.
# 
# 1. clone your repo
# 2. run `qshop` to configure and build your docs

# ### command line
# 
# `qshop` is a thin layer over the `doit` command line interface for task management. below we list the current `qshop` capabilities.

# ### python api

# In[1]:


from qshop.site import Site
get_ipython().run_line_magic('reload_ext', 'rich')


# site generates a sphinx and nikola configuration in one fell swoop. it combines information from git, github, and configuration files to generate documentation then represent some of the leading best practices.

# In[2]:


below is an example configuration generated for the `qshop` project. 


# In[3]:


site = Site()


# In[5]:


import qshop


# In[6]:


def get_subclasses(cls):
    yield cls
    for x in cls.__subclasses__():
        yield from get_subclasses(x)


# In[4]:


site.sphinx.get_config().dict()


# In[11]:


import json


# In[ ]:




