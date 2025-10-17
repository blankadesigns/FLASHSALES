const { Pool } = require('pg');

const poolConfig = {
  connectionString: process.env.DATABASE_URL,
};

// If your provider requires SSL and NODE_ENV=production, enable:
// if (process.env.NODE_ENV === 'production') {
//   poolConfig.ssl = { rejectUnauthorized: false };
// }

const pool = new Pool(poolConfig);

module.exports = {
  query: (text, params) => pool.query(text, params),
  pool,
};
