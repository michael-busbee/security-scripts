
### **Email Header Analysis**
1. **Mismatch in "From" and "Reply-To" Addresses:**
   - The sender's address may look legitimate, but the `Reply-To` address redirects to a suspicious domain.
   
2. **Unusual "Received" Chain:**
   - Inconsistent or unexpected relay servers in the `Received` headers. Check for spoofed origins or suspicious IP addresses.

3. **Forged or Suspicious SPF, DKIM, and DMARC Results:**
   - Failed or missing authentication protocols indicate the email may not be from the claimed sender.

4. **Strange Time Stamps:**
   - The email's sending time does not align with normal business hours or the sender's time zone.

---

### **Subject Line and Content Red Flags**
5. **Urgent or Threatening Language:**
   - Subject lines demanding immediate action, such as "URGENT: Account Suspension," are common in phishing attempts.

6. **Unexpected Attachments or Links:**
   - The email includes unexpected `.zip`, `.exe`, `.docm`, or `.xlsm` files. Hyperlinks that don't match the visible text are another warning.

7. **Spelling and Grammar Errors:**
   - Poor grammar or odd phrasing that does not align with professional communication standards.

8. **Generic Greetings:**
   - Phrases like "Dear Customer" or "Hello User" instead of using your actual name.

---

### **Attachment Indicators**
9. **Unusual or Suspicious File Extensions:**
   - Attachments with uncommon extensions (e.g., `.scr`, `.iso`, `.ps1`, `.vbs`) or double extensions (e.g., `invoice.pdf.exe`).

10. **Macros in Office Documents:**
    - `.doc`, `.docm`, `.xlsm` files with embedded macros prompting the user to "Enable Content" can execute malicious scripts.

11. **Unrecognized or Corrupted Content:**
    - Attachments that cannot be opened, appear corrupted, or prompt to download additional software.

---

### **Embedded URLs and Links**
12. **Obfuscated or Shortened URLs:**
    - Links using URL shorteners or containing hexadecimal obfuscation (e.g., `%20`, `%3A`).

13. **Mismatch in Link and Destination:**
    - Hover over links to check if the actual URL matches the displayed text. Suspicious redirects or misspelled domains (e.g., `m1crosoft.com`) are red flags.

14. **IP-Based URLs:**
    - URLs using IP addresses (e.g., `http://192.168.1.1`) instead of domain names.

---

### **Content and Formatting Issues**
15. **External Content Requests:**
    - Embedded images or scripts that load external content upon opening the email can track or compromise the user.

16. **Suspicious HTML Content:**
    - Malicious `.eml` files may contain embedded JavaScript or Base64-encoded payloads in the HTML body.

17. **Excessive Redirections:**
    - Content that directs the user through multiple domains before landing on a final page.

---

### **Behavioral Indicators**
18. **Request for Sensitive Information:**
    - Any request for login credentials, financial details, or personal information.

19. **Unsolicited Business or Service Offers:**
    - Emails offering unexpected refunds, rewards, or prizes.

20. **Request to Download or Execute Files:**
    - Encouragement to download software or run scripts from unknown sources.

---

### **Technical Indicators in File Analysis**
21. **Payload in Embedded Code:**
    - Look for encoded payloads within HTML or script tags when viewing the `.eml` file in a text editor.

22. **Malicious Indicators in Links:**
    - URLs linking to phishing sites, command-and-control (C2) servers, or malware downloads. Use tools like VirusTotal or URLscan.io for analysis.

23. **Anomalous Metadata:**
    - Metadata in attachments that indicate tampering or unexpected authorship details.

24. **Sandworm Indicators:**
    - Specific exploits or payload delivery mechanisms like exploiting CVE vulnerabilities.

25. **Presence of Known IOCs (Indicators of Compromise):**
    - Compare sender domains, IPs, or attachment hashes against threat intelligence databases.
