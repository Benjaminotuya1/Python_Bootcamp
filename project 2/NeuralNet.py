class AiAgent:
    def __init__(self, price):
        self.price = price
        self.is_online = True
        self.status = 'idle'
        self.total_revenue = 0

    def process_request(self, payment):
        if not self.is_online:
            return "Agent is offline. Cannot process request."
        
        if self.status == 'processing':
            return "Agent is busy. Please try again later"

        if payment < self.price:
            return f"Insufficient payment. Please provide at least {self.price} units."
        
        self.status = "processing"
        self.total_revenue += payment
        self.status = 'idle'
        return "Request processed successfully."
    

my_agent = AiAgent(5)
print('Test 1:', my_agent.process_request(10))

my_agent.status = "processing"
print('Test 2:', my_agent.process_request(10))