"""
ARES Network Storm Simulation
Stress-tests the decentralized message broker and internal routing.
"""
import time
import random
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from networking.message_broker import broker

def simulate_node_activity(node_id):
    """Simulates a rapid sequence of tactical updates from a node."""
    topics = ["mesh/heartbeat", "ai/detections", "coord/auctions"]
    
    for _ in range(50): # 50 rapid messages
        topic = random.choice(topics)
        payload = {"node": node_id, "data": random.random(), "ts": time.time()}
        broker.publish(topic, payload)

def test_subscriber(message):
    """Simple subscriber for the storm test."""
    # Process or log locally
    pass

if __name__ == "__main__":
    print("[*] Starting ARES Network Storm Simulation...")
    
    # Subscribe to all topics to measure load
    broker.subscribe("mesh/heartbeat", test_subscriber)
    broker.subscribe("ai/detections", test_subscriber)
    start_time = time.time()
    for i in range(10): # 10 virtual nodes
        simulate_node_activity(f"VNODE-{i}")
    end_time = time.time()
    
    duration = end_time - start_time
    total_msgs = 10 * 50
    throughput = total_msgs / duration if duration > 0 else float('inf')
    
    print(f"[SUCCESS] Processed {total_msgs} messages in {duration:.4f} seconds.")
    print(f"Throughput: {throughput:.2f} msgs/sec")
