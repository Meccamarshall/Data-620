#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Shamecca Marshall
# Data 620 - Web Analystics
# Week 2


# In[10]:


# Assignment: “hello, graph world”


# In[11]:


# When software developers are starting to work in a new environment, they are encouraged to start with a simple “beachhead” program. In this assignment, you’re asked to create the nodes and edges for a basic graph, such as the Krackhardt kite shown below. (You’re welcome to substitute data of your own choosing).


# In[ ]:





# In[12]:


import networkx as nx
import matplotlib.pyplot as plt


# In[13]:


# Create empty graph G for Krackhardt kite
G = nx.Graph()


# In[14]:


# Add nodes with positions
G.add_node('Carol', pos = (2, 5))
G.add_node('Andre', pos = (1, 4))
G.add_node('Fernando', pos = (3, 4))
G.add_node('Diane', pos = (2, 3))
G.add_node('Beverly', pos = (1, 2))
G.add_node('Garth', pos = (3, 2))
G.add_node('Ed', pos = (2, 1))
G.add_node('Heather', pos = (4, 3))
G.add_node('Ike', pos = (5, 3))
G.add_node('Jane', pos = (6, 3))


# In[15]:


# Add edges
G.add_edges_from([  ('Carol', 'Andre'), ('Carol', 'Fernando'), ('Carol', 'Ed'),
                    ('Andre', 'Fernando'), ('Andre', 'Diane'), ('Andre', 'Beverly'),
                    ('Beverly', 'Diane'), ('Beverly', 'Garth'), ('Beverly', 'Ed'),
                    ('Fernando', 'Diane'), ('Fernando', 'Heather'), ('Fernando', 'Garth'),
                    ('Garth', 'Diane'), ('Garth', 'Heather'), ('Garth', 'Ed'),
                    ('Ed', 'Diane'), ('Ike', 'Heather'), ('Ike', 'Jane')
                ])


# In[16]:


# Get positions of nodes in graph G
pos = nx.get_node_attributes(G, 'pos')


# In[6]:


# Draw graph nodes and edges at positions specified by pos
nx.draw(G, pos, with_labels = True)
plt.show()


# In[ ]:




