# TaameKhoob Project

A restaurant management system for my OOP course.

## What it does

- Users can see menu and customize items (add cheese, mushroom, milk, sugar, remove onion, change size)
- Build orders with multiple items
- Pay with different gateways (Zarinpal, IDPay, NextPay, Parsian)
- Deliver with different services (SnappBox, Tapsi, InHouse)
- Send notifications (Email, SMS, Push, Panel)
- Manager reports (daily, weekly, monthly sales, top items, avg prep time)

## Design patterns I used

| Singleton -> Logger, ConfigManager, DBManager 
| Factory Method -> MenuItemFactory 
| Abstract Factory -> UIFactory (Web/Mobile) 
| Builder -> OrderBuilder 
| Prototype -> OrderTemplate 
| Adapter -> Payment gateways, Delivery services 
| Decorator -> Menu items, Notifications 
| Facade -> OrderingFacade, KitchenFacade, ReportingFacade  

## Project structure

taamekhoob/
├── infrastructure/
├── menu/
├── order/
├── payment/
├── delivery/
├── notification/
├── services/
├── facades/
└── tests/

## How to run

1. Install pytest:
pip install pytest


2. Run the demo:
python final_demo.py


3. Run tests:
python -m pytest tests/ -v


## Tests

I wrote 31 tests in total:
- test_singletons.py (4)
- test_menu_decorators.py (8)
- test_builder.py (7)
- test_payment_adapters.py (7)
- test_notifications.py (6)

## Student

Atrin Yassari

