# Lab 4 – Identity & Access Management (IAM)

## Objective

This lab demonstrates Identity and Access Management (IAM) concepts on Linux by:

- Creating user roles using Linux groups
- Assigning permissions to users
- Implementing Multi-Factor Authentication (MFA)
- Automating role configuration using Terraform
- Simulating Role-Based Access Control (RBAC)

---

# Step 1 – Create User Roles

Created groups:

```bash
sudo addgroup admin_role
sudo addgroup user_role
```

Created users:

```bash
sudo adduser adminuser
sudo adduser regularuser
```

Added users to groups:

```bash
sudo usermod -aG admin_role adminuser
sudo usermod -aG user_role regularuser
```

---

# Step 2 – Configure Permissions

Created secure directories:

```bash
sudo mkdir /secure-admin
sudo mkdir /secure-user
```

Assigned permissions:

```bash
sudo chown root:admin_role /secure-admin
sudo chmod 770 /secure-admin

sudo chown root:user_role /secure-user
sudo chmod 750 /secure-user
```

---

# Step 3 – Configure MFA

Installed Google Authenticator:

```bash
sudo apt install -y libpam-google-authenticator
```

Configured PAM and SSH for MFA authentication.

Restarted SSH service:

```bash
sudo systemctl restart ssh
```

---

# Step 4 – Install Terraform

Installed Terraform manually and verified installation:

```bash
terraform --version
```

---

# Step 5 – Terraform Automation

Created Terraform configuration in `main.tf`.

Initialized Terraform:

```bash
terraform init
```

Applied configuration:

```bash
terraform apply
```

---

# Step 6 – RBAC Testing

Tested:

- adminuser has access to admin directory
- regularuser access is restricted

---

# Screenshots

All screenshots are stored in the `screenshots/` folder.

---

# Conclusion

This lab helped understand:

- IAM basics
- Linux user/group management
- MFA implementation
- Terraform automation
- RBAC concepts
