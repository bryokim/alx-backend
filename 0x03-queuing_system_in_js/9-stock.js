import express from "express";
import { createClient } from "redis";
import util from "util";

const listProducts = [
  {
    id: 1,
    name: "Suitcase 250",
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: "Suitcase 450",
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: "Suitcase 650",
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: "Suitcase 1050",
    price: 550,
    stock: 5,
  },
];

function getItemById(id) {
  for (let product of listProducts) {
    if (product.id == id) {
      return product;
    }
  }
}

const client = createClient();

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

client.get = util.promisify(client.get);

async function getCurrentReservedStockById(itemId) {
  const stock = await client.get(`item.${itemId}`).then((value) => {
    if (!value) value = 0;

    return value;
  });

  return stock;
}

const app = express();

app.get("/list_products", (req, res) => {
  const formattedProducts = [];
  for (let product of listProducts) {
    formattedProducts.push({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
    });
  }

  res.json(formattedProducts);
});

app.get("/list_products/:itemId", async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(itemId);
  if (!product) {
    res.json({ status: "Product not found" });
    return;
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);

  res.json({
    itemId,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

app.get("/reserve_product/:itemId", async (req, res) => {
  const { itemId } = req.params;

  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: "Product not found" });
    return;
  }

  const currentQuantity = Number(await getCurrentReservedStockById(itemId));

  if (product.stock - currentQuantity <= 0) {
    res.json({ status: "Not enough stock available", itemId: 1 });
    return;
  }

  reserveStockById(itemId, currentQuantity + 1);
  res.json({ status: "Reservation confirmed", itemId: 1 });
});

app.listen(1245);
