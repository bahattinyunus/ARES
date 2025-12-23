"""
ARES Auction Engine
Implements Auction-Based Task Allocation for decentralized swarm intelligence.
"""

class AuctionEngine:
    def __init__(self, node_id, node_capabilities):
        self.node_id = node_id
        self.capabilities = node_capabilities
        self.active_tasks = {} # {task_id: assignment_status}

    def calculate_bid(self, task_id, task_requirements):
        """Calculates a bid cost for a specific task."""
        if task_id in self.active_tasks:
            return float('inf') # Already engaged or task ignored

        distance = task_requirements.get('distance', 100)
        ammo = self.capabilities.get('ammo_status', 1.0)
        battery = self.capabilities.get('battery_status', 1.0)
        
        # Multi-factor cost calculation
        cost = (distance * 0.6) + (1.0 / ammo * 0.3) + (1.0 / battery * 0.1)
        return round(cost, 2)

    def process_auction(self, task_id, bids):
        """Decides the winner (lowest cost) for a specific task."""
        if not bids:
            return None
        
        winner = min(bids, key=lambda x: x['cost'])
        return {
            "task_id": task_id,
            "winner_id": winner['node_id'],
            "cost": winner['cost']
        }

    def assign_task(self, task_id):
        """Locks the node into a task."""
        self.active_tasks[task_id] = "ENGAGED"
        print(f"[!] Node {self.node_id} Engaged on Task: {task_id}")

    def complete_task(self, task_id):
        """Releases the node from a task."""
        if task_id in self.active_tasks:
            del self.active_tasks[task_id]
            print(f"[+] Task {task_id} Completed by Node {self.node_id}")
