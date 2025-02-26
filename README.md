# Odoo Shopify Stock Synchronization Module

## Overview

This Odoo module automates stock updates for Shopify by maintaining a custom table that tracks products needing synchronization. It ensures that stock availability is accurately reflected in Shopify from Odoo’s inventory.

## Features

- **Custom Stock Tracking Table**: Stores product stock updates for Shopify.
- **Automated Synchronization**: Identifies and marks products that need stock updates.
- **Shopify API Integration**: Updates stock levels using Shopify’s GraphQL API.
- **Garbage Collection**: Cleans up invalid records to maintain database integrity.

## Files in the Repository

- `__init__.py`: Initializes module components.
- `__manifest__.py`: Defines module metadata and dependencies.
- `hooks.py`: Contains a post-installation hook to create the stock tracking table.
- `products.py`: Adds a boolean field to mark products as Shopify-enabled.
- `stock_avaliablity.py`: Handles marking products as needing stock updates and manages cleanup tasks.

## Setup & Configuration

### Prerequisites

- Odoo 15 installed
- Shopify API credentials
- Required Odoo dependencies (`wwuk_stock_availability`, `wwuk_product`)

### Configuration

- Ensure products that should sync with Shopify have `shopify_product` enabled.
- The module automatically tracks stock updates and stores them in `stock_availability_dirty_shopify`.

## How It Works

1. **Tracking Stock Updates**:
   - When stock availability changes, the `_dirty` function logs product IDs that need syncing.
   - Related parent products are also marked for updates.
2. **Shopify Synchronization**:
   - External scripts or cron jobs can fetch records from `stock_availability_dirty_shopify` and update Shopify.
3. **Database Cleanup**:
   - The `_gc_invalid_shopify_records` function removes orphaned records.

## Logs & Debugging

- Errors related to stock tracking can be found in the Odoo logs.
- Ensure Shopify API credentials are correctly set if synchronization issues occur.

## Future Enhancements

- Add automated cron jobs for stock updates.
- Implement retry mechanisms for failed Shopify API calls.
- Optimize parent product determination for performance improvements.

## License

This module is proprietary and should not be shared without permission.

