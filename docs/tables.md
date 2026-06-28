# 1. Transaction Status (fondamentale)

Questa è la base di tutto il flusso.

| Codice       | Nome       | Descrizione                               |
| ------------ | ---------- | ----------------------------------------- |
| `PENDING`    | Pending    | Transazione creata ma non ancora eseguita |
| `PROCESSING` | Processing | In fase di esecuzione (utile per async)   |
| `COMPLETED`  | Completed  | Eseguita con successo                     |
| `FAILED`     | Failed     | Fallita (errore logico o tecnico)         |
| `CANCELLED`  | Cancelled  | Annullata prima dell’esecuzione           |

---

# 2. Transaction Type

| Codice     | Nome     | Descrizione                   |
| ---------- | -------- | ----------------------------- |
| `TRANSFER` | Transfer | Trasferimento tra due account |
| `DEPOSIT`  | Deposit  | Accredito su account          |
| `WITHDRAW` | Withdraw | Prelievo                      |
| `FEE`      | Fee      | Commissione                   |
| `REFUND`   | Refund   | Rimborso                      |

---

# 3. Failure Reason Codes

Serve per non avere solo `FAILED`, ma capire *perché*.

| Codice               | Nome               | Descrizione         |
| -------------------- | ------------------ | ------------------- |
| `INSUFFICIENT_FUNDS` | Insufficient Funds | Saldo insufficiente |
| `ACCOUNT_NOT_FOUND`  | Account Not Found  | Account inesistente |
| `ACCOUNT_FROZEN`     | Account Frozen     | Account bloccato    |
| `CURRENCY_MISMATCH`  | Currency Mismatch  | Valute diverse      |
| `VALIDATION_ERROR`   | Validation Error   | Input non valido    |
| `SYSTEM_ERROR`       | System Error       | Errore interno      |

---

# 4. Ledger Entry Type (per il passo successivo)

Quando passerai al **double-entry accounting**:

| Codice   | Nome   | Descrizione       |
| -------- | ------ | ----------------- |
| `DEBIT`  | Debit  | Diminuzione fondi |
| `CREDIT` | Credit | Aumento fondi     |

---

# 5. Ledger Account Types (modello bancario reale)

| Codice      | Nome      | Descrizione                |
| ----------- | --------- | -------------------------- |
| `ASSET`     | Asset     | Conti clienti              |
| `LIABILITY` | Liability | Debiti banca verso clienti |
| `REVENUE`   | Revenue   | Commissioni                |
| `EXPENSE`   | Expense   | Costi                      |

---

# 6. Transaction Flow (Flow Chart logico)

### Standard Transfer Flow

```
[START]
   ↓
VALIDATION
   ↓
CREATE TRANSACTION (PENDING)
   ↓
CHECK BUSINESS RULES
   ↓
EXECUTE TRANSFER
   ↓
SUCCESS? ─── NO ───→ FAILED
   ↓ YES
UPDATE ACCOUNTS
   ↓
MARK COMPLETED
   ↓
[END]
```
---

# 7. Legend per Flow Chart

Usa sempre questa legenda nei tuoi diagrammi:

| Simbolo      | Significato                          |
| ------------ | ------------------------------------ |
| ⬜ Rectangle  | Process (es. "Execute transfer")     |
| 🔷 Diamond   | Decision (es. "Balance sufficient?") |
| ⭕ Circle     | Start / End                          |
| ➡️ Arrow     | Flow                                 |
| 🗂️ Cylinder | Database                             |