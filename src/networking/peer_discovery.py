"""
ARES Peer Discovery Module
Handles mDNS and DHT based discovery of tactical nodes in the mesh.
"""

import time
import logging

class PeerDiscovery:
    def __init__(self, node_id, interface="wlan0"):
        self.node_id = node_id
        self.interface = interface
        self.peers = {} # {peer_id: last_seen_timestamp}
        self.is_running = False
        logging.info(f"Initialized Discovery on {interface} for Node {node_id}")

    def start_broadcast(self):
        """Starts advertising node presence and sending heartbeats."""
        self.is_running = True
        print(f"[*] Node {self.node_id} broadcasting heartbeats...")
        # In a real app, this would run in a separate thread
        while self.is_running:
            self._send_heartbeat()
            self._cleanup_stale_peers()
            time.sleep(2) # 2-second interval for mesh stability

    def _send_heartbeat(self):
        """Sends a tactical heartbeat packet to the mesh."""
        # Simulated heartbeat packet
        pass

    def _cleanup_stale_peers(self):
        """Removes peers that haven't sent a heartbeat for more than 10 seconds."""
        current_time = time.time()
        stale_threshold = 10
        stale_peers = [pid for pid, last_seen in self.peers.items() if (current_time - last_seen) > stale_threshold]
        
        for pid in stale_peers:
            print(f"[!] Peer {pid} lost connection (Heartbeat Timeout)")
            del self.peers[pid]

    def on_heartbeat_received(self, peer_id):
        """Callback when a heartbeat is received from a peer."""
        if peer_id not in self.peers:
            print(f"[+] New Peer Discovered: {peer_id}")
        self.peers[peer_id] = time.time()

    def listen_for_peers(self):
        """Listens for other nodes joining the network."""
        print("[*] Listening for peers...")
        # TODO: Implement DHT discovery
        pass

if __name__ == "__main__":
    discovery = PeerDiscovery(node_id="ARES-NODE-01")
    discovery.start_broadcast()
