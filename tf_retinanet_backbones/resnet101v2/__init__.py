"""
Copyright 2017-2019 Fizyr (https://fizyr.com)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from .resnet101v2 import ResNet101V2Backbone
from tf_retinanet.utils.config import set_defaults


default_config = {'type': 'resnet101v2'}


def from_config(config, **kwargs):
	""" Create a ResNet101v2 backbone from a backbone configuration dict.
	# Arguments
		config: backbone configuration dict.
	# Returns
		backbone: ResNet101v2 backbone for tf-retinanet.
	"""
	return ResNet101V2Backbone(set_defaults(config, default_config), **kwargs)
