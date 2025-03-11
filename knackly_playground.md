# Knackly Basics Guide

## 1. Introduction to Knackly
Knackly is a document automation platform that allows users to generate legal and business documents using dynamic templates. It uses variables, conditions, loops, and formatting functions to automate content generation.

---

## 2. Variables in Knackly
Variables are placeholders for dynamic content.

### **Basic Variable Usage**
```knackly
{{ ClientName }}
{{ LoanAmount }}
```

### **Setting Default Values**
```knackly
{{ ClientName | Default("John Doe") }}
```

---

## 3. Conditional Logic (IF-ELSE)
Use `IF` statements to insert text based on conditions.

### **Example:** Governing Law Clause
```knackly
[IF State = "California"]
    This contract is governed by the laws of California.
[ELSEIF State = "Texas"]
    This contract is governed by the laws of Texas.
[ELSE]
    This contract is governed by the laws of the relevant jurisdiction.
[END IF]
```

---

## 4. Loops (REPEAT)
Use `REPEAT` to iterate through lists of data.

### **Example:** Listing Multiple Beneficiaries
```knackly
[REPEAT Beneficiary IN BeneficiariesList]
    {{ Beneficiary.FirstName }} {{ Beneficiary.LastName }}
[END REPEAT]
```

---

## 5. Functions in Knackly
Knackly uses **pipe (`|`) notation** to apply functions to variables.

### **Common Functions:**

| Function         | Description                           | Example |
|-----------------|---------------------------------------|---------|
| `UpperCase`     | Converts text to uppercase           | `{{ ClientName | UpperCase }}` → **"JOHN DOE"** |
| `LowerCase`     | Converts text to lowercase           | `{{ ClientName | LowerCase }}` → **"john doe"** |
| `Capitalize`    | Capitalizes the first letter         | `{{ DocumentType | Capitalize }}` → **"Contract"** |
| `NumberToWords` | Converts numbers to words           | `{{ LoanAmount | NumberToWords }}` → **"One Thousand"** |
| `FormatDate`    | Formats a date                      | `{{ Today() | FormatDate("MMMM d, yyyy") }}` → **"March 10, 2025"** |

---

## 6. Using Dates in Knackly
### **Insert the Current Date**
```knackly
{{ Today() }}
```

### **Calculate a Future Date**
```knackly
{{ Today() + 30 }}
```
(Outputs a date 30 days from today.)

---

## 7. Pluralization for Grammar Correction
### **Example:** Handling Singular vs. Plural Wording
```knackly
The beneficiary shall receive 
[IF NumBeneficiaries = 1]
    the entirety of the estate.
[ELSE]
    an equal share of the estate among all beneficiaries.
[END IF]
```

---

## 8. Conditional Paragraphs
### **Example:** Including an Arbitration Clause
```knackly
[IF IncludeArbitration = "Yes"]
    The parties agree to resolve disputes through binding arbitration.
[END IF]
```

---

## 9. Formatting Numbers and Currency
### **Example:** Formatting a Currency Value
```knackly
{{ LoanAmount | FormatNumber("$#,##0.00") }}
```
(Formats **1000** as **$1,000.00**.)

---

## 10. Dynamic Signature Blocks
### **Example:** Adjusting Signatures Based on Buyer Type
```knackly
[IF BuyerType = "Individual"]
    Buyer: {{ BuyerFirstName }} {{ BuyerLastName }}
    Signature: ____________________
[ELSE]
    Buyer: {{ CompanyName }}
    By: {{ RepresentativeName }}, {{ RepresentativeTitle }}
    Signature: ____________________
[END IF]
```

---

## 11. Best Practices for Knackly Templates
✅ Keep variable names **descriptive and consistent**.  
✅ Use `IF-ELSE` logic to handle **variations in legal text**.  
✅ Apply `REPEAT` for **listing multiple entities** dynamically.  
✅ Format **dates, numbers, and text** using built-in functions.  
✅ Test templates thoroughly to ensure correct document generation.  

---

## 12. Summary
Knackly provides powerful tools to automate legal and business documents. By leveraging **variables, conditions, loops, and functions**, you can create dynamic and customizable templates that streamline document generation.

---
