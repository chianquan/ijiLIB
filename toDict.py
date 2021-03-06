# -*- coding: utf-8 -*-
__author__ = 'Yuanzhou Qiu'

class Dict(dict):
	def __init__(self, names=(), values=(), **kw):
		super(Dict, self).__init__(**kw)
		for k, v in zip(names, values):
			self[k] = v
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError("'Dict' object has no attribute '%s'." % key)
	def __setattr__(self, key, value):
		self[key] = value