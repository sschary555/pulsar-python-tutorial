#!/usr/bin/env python
#
# Copyright 2017 Streamlio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pulsar

# Create a Pulsar client instance. The instance can be shared across multiple
# producers and consumers
client = pulsar.Client('pulsar://localhost:6650')

# Create a producer on the topic. If the topic doesn't exist
# it will be automatically created
producer = client.create_producer(
                'persistent://sample/standalone/ns1/my-topic')

for i in range(10):
    content = 'hello-pulsar-%d' % i
    # Publish a message and wait until it is persisted
    producer.send(content)
    print('Published message: "%s"' % content)

client.close()
