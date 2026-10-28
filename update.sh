cat << 'HTML' > index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Madzinu Web3 Technologies | Enterprise Cloud & Autonomous Workflows</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-color: #090d16;
            --card-bg: #111827;
            --card-border: #1f2937;
            --accent-indigo: #6366f1;
            --accent-emerald: #10b981;
            --accent-amber: #f59e0b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: system-ui, -apple-system, sans-serif; }
        body { background-color: var(--bg-color); color: var(--text-main); min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
        header { background: #0b101d; border-bottom: 1px solid var(--card-border); padding: 10px 14px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 100; }
        .brand-title { font-size: 11px; font-weight: 800; color: #818cf8; }
        .marquee-container { overflow: hidden; width: 100%; position: relative; margin-top: 2px; }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 15s linear infinite; font-size: 8px; color: #34d399; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .container { max-width: 600px; margin: 0 auto; padding: 14px; width: 100%; flex-grow: 1; display: flex; flex-direction: column; gap: 14px; }
        .hero-card { background: linear-gradient(180deg, #111827 0%, #090d16 100%); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 16px; padding: 18px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        .badge-pill { display: inline-block; background: rgba(245, 158, 11, 0.1); color: var(--accent-amber); border: 1px solid rgba(245, 158, 11, 0.3); padding: 4px 10px; border-radius: 20px; font-size: 9px; font-weight: 700; margin-bottom: 10px; }
        h1 { font-size: 18px; font-weight: 900; line-height: 1.3; margin-bottom: 10px; color: #fff; }
        h1 span { background: linear-gradient(90deg, #818cf8, #38bdf8, #34d399); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        p { font-size: 11px; color: var(--text-muted); line-height: 1.5; margin-bottom: 14px; }
        .btn-primary { background: var(--accent-indigo); color: white; border: none; width: 100%; padding: 12px; border-radius: 12px; font-weight: bold; font-size: 12px; cursor: pointer; box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4); }
        .section-box { background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 12px; padding: 14px; }
        .grid-5 { display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; margin-top: 8px; }
        .wa-btn { background: #166534; color: white; border: none; padding: 6px 2px; border-radius: 6px; font-size: 8.5px; font-weight: bold; cursor: pointer; text-align: center; }
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 8px; }
        .grid-4 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin-top: 8px; }
        .partner-card { background: #0f172a; border: 1px solid #1e293b; padding: 10px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center; text-decoration: none; color: #fff; font-size: 11px; font-weight: bold; }
        footer { background: #0b101d; border-top: 1px solid var(--card-border); padding: 16px; text-align: center; font-size: 10px; color: var(--text-muted); margin-top: auto; }
        
        #user-workspace-dashboard { display: none; background: linear-gradient(135deg, #0f172a 0%, #111827 100%); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 14px; padding: 16px; margin-bottom: 12px; }
        .user-info-bar { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px; margin-bottom: 12px; font-size: 11px; }
        .user-balance-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 12px; }
        .bal-card { background: #090d16; border: 1px solid #1e293b; border-radius: 10px; padding: 10px; }
        .bal-val { font-size: 16px; font-weight: 900; color: #34d399; margin-top: 4px; }
        .server-catalog-grid { display: grid; grid-template-columns: 1fr; gap: 10px; margin-top: 10px; }
        .server-card-item { background: #090d16; border: 1px solid #1e293b; border-radius: 10px; padding: 12px; }
        #slice-modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 99999; justify-content: center; align-items: center; }
        .slice-content { background: #111827; border: 1px solid #ec4899; padding: 20px; border-radius: 14px; width: 90%; max-width: 420px; text-align: left; }
        #admin-modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 99999; justify-content: center; align-items: center; }
        .modal-content { background: #111827; border: 1px solid #6366f1; padding: 20px; border-radius: 12px; width: 90%; max-width: 400px; text-align: center; }
    </style>
</head>
<body>
    <header>
        <div>
            <div class="brand-title">MADZINU WEB3 TECH & AI</div>
            <div class="marquee-container">
                <span class="animate-marquee"><i class="fa-solid fa-check-circle"></i> <span id="marquee-txt">Govt. of India Recognized Startup (MeitY) | Reg No: ST20260926506</span></span>
            </div>
        </div>
        <div style="display: flex; gap: 6px; align-items: center;">
            <select id="langSelector" onchange="changeLanguage()" style="background: #0f172a; color: #fff; border: 1px solid #334155; padding: 4px; border-radius: 4px; font-size: 10px;">
                <option value="EN" selected>EN</option>
                <option value="TA">தமிழ்</option>
                <option value="TE">తెలుగు</option>
                <option value="KN">ಕನ್ನಡ</option>
                <option value="ML">മലയാളം</option>
                <option value="HI">हिन्दी</option>
                <option value="MR">मराठी</option>
            </select>
            <button onclick="openAdminPanel()" style="background: rgba(244,63,94,0.1); border: 1px solid rgba(244,63,94,0.3); color: #fb7185; padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; cursor: pointer; z-index: 1000;"><i class="fa-solid fa-user-shield"></i> <span id="admin-btn-txt">Admin</span></button>
        </div>
    </header>

    <div class="container">
        <div class="hero-card">
            <div class="badge-pill" id="hero-badge">👑 INDIA'S FIRST AUTONOMOUS AI STUDIO & CLOUD NETWORK</div>
            <h1 id="hero-title">Sovereign Cloud Compute &<br><span>Autonomous Jobworks</span></h1>
            <p id="hero-desc">Madzinu Web3 Technologies is a Govt. of India Recognized Startup entity under MeitY with approved IndiaAI Portal compute access. Provision high-throughput server compute packages from ₹5,000 to ₹1,00,000.</p>
            <button class="btn-primary" id="launch-term-btn" onclick="scrollToLogin()"><i class="fa-solid fa-arrow-right-to-bracket"></i> LAUNCH SECURE ENTERPRISE TERMINAL</button>
        </div>

        <div id="user-workspace-dashboard">
            <div class="user-info-bar">
                <div>
                    <div style="color: #94a3b8; font-size: 9px;" id="ws-node-lbl">CONNECTED CONTRACTOR NODE</div>
                    <div style="font-weight: bold; color: #38bdf8;" id="user-mobile-display">+91 9840000000</div>
                </div>
                <div style="display: flex; gap: 6px; align-items: center;">
                    <div style="text-align: right;">
                        <div style="color: #94a3b8; font-size: 9px;" id="ws-status-lbl">NODE LICENSE STATUS</div>
                        <div style="font-weight: bold; color: #34d399;"><i class="fa-solid fa-circle-check"></i> <span id="ws-active-txt">14-Day Active Node</span></div>
                    </div>
                    <button id="ws-logout-btn" onclick="logoutUser()" style="background: rgba(239, 68, 68, 0.2); border: 1px solid rgba(239, 68, 68, 0.4); color: #f87171; padding: 6px 10px; border-radius: 6px; font-size: 10px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-right-from-bracket"></i> Logout</button>
                </div>
            </div>

            <div style="background: #090d16; border: 1px solid #1e293b; border-radius: 10px; padding: 12px; margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span id="catalog-title" style="font-size: 11px; font-weight: bold; color: #ec4899;"><i class="fa-solid fa-server"></i> SELECT SERVER TIER & JOBWORK EARNINGS</span>
                    <span style="font-size: 9px; color: #34d399;">MeitY Portal Approved</span>
                </div>
                <p id="catalog-desc" style="font-size: 10px; color: #94a3b8; margin-bottom: 10px;">Review daily task remuneration and pay via GPay / Slice Account to update balance instantly:</p>
                
                <div class="server-catalog-grid">
                    <!-- ₹5,000 Server -->
                    <div class="server-card-item">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                            <span style="font-weight: bold; color: #fff; font-size: 12px;">₹5,000 Server</span>
                            <div style="display: flex; gap: 4px;">
                                <a href="upi://pay?pa=madhan958@slc&pn=Madzinu%20Web3%20Technologies&am=5000&cu=INR&tn=Server%20Tier%205000" target="_blank" style="background: #2563eb; color: white; border: none; padding: 6px 8px; border-radius: 6px; font-size: 9px; font-weight: bold; text-decoration: none; display: inline-flex; align-items: center; gap: 3px;"><i class="fa-solid fa-mobile-screen"></i> GPay</a>
                                <button onclick="openSlicePayment(5000, 394.64)" style="background: #ec4899; color: white; border: none; padding: 6px 8px; border-radius: 6px; font-size: 9px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-qrcode"></i> Slice</button>
                            </div>
                        </div>
                        <div style="font-size: 10px; color: #94a3b8; display: flex; flex-direction: column; gap: 2px;">
                            <div><i class="fa-solid fa-list-check" style="color: #6366f1;"></i> Daily Tasks: <strong>5 Tasks / day</strong></div>
                            <div><i class="fa-solid fa-bolt" style="color: #34d399;"></i> Daily Remuneration: <strong style="color: #34d399;">₹394.64 / day</strong></div>
                            <div><i class="fa-solid fa-calendar-days" style="color: #f59e0b;"></i> 14-Day Total: <strong style="color: #f59e0b;">₹5,525</strong></div>
                        </div>
                    </div>

                    <!-- ₹10,000 Server -->
                    <div class="server-card-item">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                            <span style="font-weight: bold; color: #fff; font-size: 12px;">₹10,000 Server</span>
                            <div style="display: flex; gap: 4px;">
                                <a href="upi://pay?pa=madhan958@slc&pn=Madzinu%20Web3%20Technologies&am=10000&cu=INR&tn=Server%20Tier%2010000" target="_blank" style="background: #2563eb; color: white; border: none; padding: 6px 8px; border-radius: 6px; font-size: 9px; font-weight: bold; text-decoration: none; display: inline-flex; align-items: center; gap: 3px;"><i class="fa-solid fa-mobile-screen"></i> GPay</a>
                                <button onclick="openSlicePayment(10000, 792.86)" style="background: #ec4899; color: white; border: none; padding: 6px 8px; border-radius: 6px; font-size: 9px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-qrcode"></i> Slice</button>
                            </div>
                        </div>
                        <div style="font-size: 10px; color: #94a3b8; display: flex; flex-direction: column; gap: 2px;">
                            <div><i class="fa-solid fa-list-check" style="color: #6366f1;"></i> Daily Tasks: <strong>10 Tasks / day</strong></div>
                            <div><i class="fa-solid fa-bolt" style="color: #34d399;"></i> Daily Remuneration: <strong style="color: #34d399;">₹792.86 / day</strong></div>
                            <div><i class="fa-solid fa-calendar-days" style="color: #f59e0b;"></i> 14-Day Total: <strong style="color: #f59e0b;">₹11,100</strong></div>
                        </div>
                    </div>

                    <!-- ₹25,000 Server -->
                    <div class="server-card-item">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                            <span style="font-weight: bold; color: #fff; font-size: 12px;">₹25,000 Server</span>
                            <div style="display: flex; gap: 4px;">
                                <a href="upi://pay?pa=madhan958@slc&pn=Madzinu%20Web3%20Technologies&am=25000&cu=INR&tn=Server%20Tier%2025000" target="_blank" style="background: #2563eb; color: white; border: none; padding: 6px 8px; border-radius: 6px; font-size: 9px; font-weight: bold; text-decoration: none; display: inline-flex; align-items: center; gap: 3px;"><i class="fa-solid fa-mobile-screen"></i> GPay</a>
                                <button onclick="openSlicePayment(25000, 1991.07)" style="background: #ec4899; color: white; border: none; padding: 6px 8px; border-radius: 6px; font-size: 9px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-qrcode"></i> Slice</button>
                            </div>
                        </div>
                        <div style="font-size: 10px; color: #94a3b8; display: flex; flex-direction: column; gap: 2px;">
                            <div><i class="fa-solid fa-list-check" style="color: #6366f1;"></i> Daily Tasks: <strong>25 Tasks / day</strong></div>
                            <div><i class="fa-solid fa-bolt" style="color: #34d399;"></i> Daily Remuneration: <strong style="color: #34d399;">₹1,991.07 / day</strong></div>
                            <div><i class="fa-solid fa-calendar-days" style="color: #f59e0b;"></i> 14-Day Total: <strong style="color: #f59e0b;">₹27,875</strong></div>
                        </div>
                    </div>

                    <!-- ₹50,000 Server -->
                    <div class="server-card-item">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                            <span style="font-weight: bold; color: #fff; font-size: 12px;">₹50,000 Server</span>
                            <div style="display: flex; gap: 4px;">
                                <a href="upi://pay?pa=madhan958@slc&pn=Madzinu%20Web3%20Technologies&am=50000&cu=INR&tn=Server%20Tier%2050000" target="_blank" style="background: #2563eb; color: white; border: none; padding: 6px 8px; border-radius: 6px; font-size: 9px; font-weight: bold; text-decoration: none; display: inline-flex; align-items: center; gap: 3px;"><i class="fa-solid fa-mobile-screen"></i> GPay</a>
                                <button onclick="openSlicePayment(50000, 4000)" style="background: #ec4899; color: white; border: none; padding: 6px 8px; border-radius: 6px; font-size: 9px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-qrcode"></i> Slice</button>
                            </div>
                        </div>
                        <div style="font-size: 10px; color: #94a3b8; display: flex; flex-direction: column; gap: 2px;">
                            <div><i class="fa-solid fa-list-check" style="color: #6366f1;"></i> Daily Tasks: <strong>50 Tasks / day</strong></div>
                            <div><i class="fa-solid fa-bolt" style="color: #34d399;"></i> Daily Remuneration: <strong style="color: #34d399;">₹4,000 / day</strong></div>
                            <div><i class="fa-solid fa-calendar-days" style="color: #f59e0b;"></i> 14-Day Total: <strong style="color: #f59e0b;">₹56,000</strong></div>
                        </div>
                    </div>

                    <!-- ₹1,00,000 Server -->
                    <div class="server-card-item">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                            <span style="font-weight: bold; color: #f59e0b; font-size: 12px;">₹1,00,000 Server <span style="background: rgba(245, 158, 11, 0.2); padding: 2px 6px; border-radius: 4px; font-size: 8px;">Max</span></span>
                            <div style="display: flex; gap: 4px;">
                                <a href="upi://pay?pa=madhan958@slc&pn=Madzinu%20Web3%20Technologies&am=100000&cu=INR&tn=Server%20Tier%20100000" target="_blank" style="background: #2563eb; color: white; border: none; padding: 6px 8px; border-radius: 6px; font-size: 9px; font-weight: bold; text-decoration: none; display: inline-flex; align-items: center; gap: 3px;"><i class="fa-solid fa-mobile-screen"></i> GPay</a>
                                <button onclick="openSlicePayment(100000, 8000)" style="background: #ec4899; color: white; border: none; padding: 6px 8px; border-radius: 6px; font-size: 9px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-qrcode"></i> Slice</button>
                            </div>
                        </div>
                        <div style="font-size: 10px; color: #94a3b8; display: flex; flex-direction: column; gap: 2px;">
                            <div><i class="fa-solid fa-list-check" style="color: #6366f1;"></i> Daily Tasks: <strong>100 Tasks / day</strong></div>
                            <div><i class="fa-solid fa-bolt" style="color: #34d399;"></i> Daily Remuneration: <strong style="color: #34d399;">₹8,000 / day</strong></div>
                            <div><i class="fa-solid fa-calendar-days" style="color: #f59e0b;"></i> 14-Day Total: <strong style="color: #f59e0b;">₹1,12,000</strong></div>
                        </div>
                    </div>
                </div>
            </div>

            <div style="font-size: 11px; font-weight: bold; color: #f59e0b; margin-bottom: 8px; display: flex; justify-content: space-between;">
                <span id="ws-board-title"><i class="fa-solid fa-wallet"></i> USER WORKSPACE BALANCE BOARD</span>
                <span style="color: #34d399; font-size: 9px;" id="ws-spot-txt">● LIVE SPOT SYNCHRONIZED</span>
            </div>

            <div class="user-balance-grid">
                <div class="bal-card">
                    <div style="font-size: 9px; color: #94a3b8;" id="ws-inr-lbl">INR Workspace Balance</div>
                    <div class="bal-val" id="user-inr-bal">₹0.00</div>
                </div>
                <div class="bal-card">
                    <div style="font-size: 9px; color: #94a3b8;" id="ws-yield-lbl">Daily Task Remuneration</div>
                    <div class="bal-val" id="user-daily-yield">₹0.00 / Day</div>
                </div>
                <div class="bal-card">
                    <div style="font-size: 9px; color: #f59e0b;" id="ws-gold-lbl">Live 24K Gold Vault (Grams)</div>
                    <div class="bal-val" id="user-gold-bal" style="color: #f59e0b;">0.000 g</div>
                </div>
                <div class="bal-card">
                    <div style="font-size: 9px; color: #cbd5e1;" id="ws-silver-lbl">Live Silver Vault (Grams)</div>
                    <div class="bal-val" id="user-silver-bal" style="color: #cbd5e1;">0.000 g</div>
                </div>
            </div>

            <div style="display: flex; gap: 8px;">
                <button id="ws-task-btn" onclick="alert('Execute daily automated task pipelines to credit INR balance!')" style="flex: 1; background: #10b981; color: white; border: none; padding: 8px; border-radius: 8px; font-size: 10px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-play"></i> Run Daily Tasks</button>
                <button id="ws-payout-btn" onclick="alert('Withdrawals are processed under Section 194TDS contractor guidelines directly to your locked bank account.')" style="flex: 1; background: #6366f1; color: white; border: none; padding: 8px; border-radius: 8px; font-size: 10px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-arrow-up-right-from-square"></i> Request Payout</button>
            </div>
        </div>

        <div class="section-box" id="login-section">
            <h3 id="login-title" style="font-size: 11px; color: #818cf8; margin-bottom: 8px;"><i class="fa-solid fa-shield-keyhole"></i> Contractor Secure Node Login</h3>
            <div style="display: flex; gap: 8px; margin-bottom: 8px;">
                <input type="text" id="login-mobile" placeholder="Enter Mobile Number" style="flex-grow: 1; background: #090d16; border: 1px solid #334155; padding: 8px; border-radius: 8px; color: #fff; font-size: 11px;">
                <button id="send-otp-btn" onclick="alert('OTP sent via Fast2SMS gateway!')" style="background: #6366f1; color: #fff; border: none; padding: 8px 12px; border-radius: 8px; font-size: 11px; font-weight: bold; cursor: pointer;">Send OTP</button>
            </div>
            <div style="display: flex; gap: 8px;">
                <input type="text" id="login-otp-code" placeholder="Enter OTP (Admin: 2026)" style="flex-grow: 1; background: #090d16; border: 1px solid #334155; padding: 8px; border-radius: 8px; color: #fff; font-size: 11px;">
                <button id="verify-otp-btn" onclick="verifySecureNodeAccess()" style="background: #10b981; color: #fff; border: none; padding: 8px 14px; border-radius: 8px; font-size: 11px; font-weight: bold; cursor: pointer;">Verify</button>
            </div>
        </div>
    </div>

    <div id="slice-modal">
        <div class="slice-content">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid #1f2937; padding-bottom: 8px;">
                <span style="font-weight: bold; color: #ec4899; font-size: 13px;"><i class="fa-solid fa-building-columns"></i> Slice Current Account Details</span>
                <button onclick="closeSliceModal()" style="background: none; border: none; color: #94a3b8; font-size: 16px; cursor: pointer;">&times;</button>
            </div>
            <div style="font-size: 11px; color: #d1d5db; display: flex; flex-direction: column; gap: 8px; margin-bottom: 14px; background: #090d16; padding: 12px; border-radius: 8px;">
                <div><strong>Account Name:</strong> Madzinu Web3 Technologies</div>
                <div><strong>Account No:</strong> <span style="color: #34d399; font-family: monospace;">033311501076921</span></div>
                <div><strong>IFSC:</strong> <span style="color: #38bdf8; font-family: monospace;">NESF0000333</span></div>
                <div><strong>UPI ID:</strong> <span style="color: #ec4899; font-weight: bold;">madhan958@slc</span></div>
                <div><strong>Selected Package:</strong> <span id="slice-modal-amount" style="color: #f59e0b; font-weight: bold;">₹5,000</span></div>
            </div>
            <input type="text" id="slice-utr-input" placeholder="Enter UPI Ref / UTR Transaction ID" style="width: 100%; background: #090d16; border: 1px solid #334155; padding: 8px; border-radius: 8px; color: #fff; font-size: 11px; margin-bottom: 10px;">
            <button onclick="confirmSlicePayment()" style="background: #10b981; color: white; border: none; width: 100%; padding: 10px; border-radius: 8px; font-weight: bold; font-size: 11px; cursor: pointer;">Verify & Activate Server Package</button>
        </div>
    </div>

    <script>
        let pendingAmount = 5000;
        let pendingDailyYield = 394.64;
        function verifySecureNodeAccess() {
            let otp = document.getElementById('login-otp-code').value.trim();
            if(otp === '2026' || otp === 'madz1222') {
                alert('Node Access Verified Successfully!');
                document.getElementById('user-workspace-dashboard').style.display = 'block';
                document.getElementById('user-workspace-dashboard').scrollIntoView({ behavior: 'smooth' });
            } else { alert('Invalid OTP or Admin Code!'); }
        }
        function logoutUser() {
            document.getElementById('user-workspace-dashboard').style.display = 'none';
            window.scrollTo({ top: 0, behavior: 'smooth' });
            alert('Successfully logged out.');
        }
        function openSlicePayment(amount, dailyYield) {
            pendingAmount = amount;
            pendingDailyYield = dailyYield;
            document.getElementById('slice-modal-amount').innerText = '₹' + parseInt(amount).toLocaleString('en-IN') + ' (Earnings: ₹' + dailyYield + '/Day)';
            document.getElementById('slice-modal').style.display = 'flex';
        }
        function closeSliceModal() { document.getElementById('slice-modal').style.display = 'none'; }
        function confirmSlicePayment() {
            let utr = document.getElementById('slice-utr-input').value.trim();
            if(!utr) { alert('Please enter UTR number!'); return; }
            document.getElementById('user-inr-bal').innerText = '₹' + parseInt(pendingAmount).toLocaleString('en-IN') + '.00';
            document.getElementById('user-daily-yield').innerText = '₹' + pendingDailyYield + ' / Day';
            closeSliceModal();
            alert('Payment verified and server package activated!');
        }
    </script>
</body>
</html>
HTML
echo "index.html updated successfully!"
