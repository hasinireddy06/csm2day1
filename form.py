<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Student Profile</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      color: #000;
      background: #fff;
      margin: 30px;
    }
    h1, h2, h3 {
      margin: 0;
      padding: 0;
      font-weight: bold;
    }
    h2 {
      font-size: 20px;
      text-align: center;
    }
    .header-small {
      font-size: 12px;
    }
    table {
      width: 100%;
      border: 1px solid #222;
      border-collapse: collapse;
      margin-bottom: 10px;
    }
    th, td {
      border: 1px solid #222;
      font-size: 13px;
      padding: 5px;
      vertical-align: top;
    }
    input, textarea {
      width: 100%;
      border: none;
      font-size: 13px;
      font-family: inherit;
    }
    textarea {
      resize: vertical;
    }
    .noborder {
      border: none !important;
    }
    .subhead {
      text-align: center;
      font-weight: bold;
      margin: 12px 0;
    }
    .college-logo {
      width: 275px;
      height: 175px;
      object-fit: contain;
      margin-right: 18px;
    }
    .header-row {
      display: flex;
      align-items: center;
      gap: 20px;
    }
  </style>
</head>
<body>
  <div class="form-outer">
    <div class="header-row">
      <img src="https://lh5.googleusercontent.com/proxy/GFtlNbBZDFw6RzkhCVF56ScxB4zKBg2Evqc6iHC_gwOXVkPrixqPXa1mb7hpjqQhkE9wDa2o77xY4b7RaX4hnG_e2ZY"
           alt="College Logo" class="college-logo" />
      <div style="text-align: center; line-height: 1.6;">
        <h2>GAYATRI VIDYA PARISHAD COLLEGE OF ENGINEERING FOR WOMEN(A)</h2>
        <div style="font-size: 14px;">
          Madhurawada :: Visakhapatnam – 530 048<br>
          (Approved by AICTE, New Delhi and Permanently Affiliated to Andhra University, Visakhapatnam)<br>
          Accredited by NAAC with “A” from 2022 to 2027<br>
          CSE, ECE and IT Courses Accredited by NBA (2019–2022) and Re-accredited (2022–2025)<br>
          EEE Course Accredited by NBA (2023–2026)<br>
          <strong>Ph : 0891-2739144</strong>&nbsp;&nbsp;
          Fax : 0891-2562639&nbsp;&nbsp;
          e-mail: gvpcew@gmail.com&nbsp;&nbsp;
          Website: www.gvpcew.ac.in
        </div>
      </div>
    </div>
  </div>

  <hr style="margin: 12px 0;">
  <h2>STUDENT PROFILE</h2>

  <!-- Basic Details -->
  <table>
    <tr>
      <th>H T NO.</th>
      <th>NAME OF THE STUDENT (as per SSC)</th>
      <th>BRANCH</th>
    </tr>
    <tr>
      <td><input type="text"></td>
      <td><input type="text"></td>
      <td><input type="text"></td>
    </tr>
  </table>

  <table>
    <tr>
      <th>Date of Birth (as per SSC)</th>
      <th>AADHAR No. (self)</th>
      <th>Mobile No. (Self)</th>
      <th>e-mail ID</th>
    </tr>
    <tr>
      <td><input type="date"></td>
      <td><input type="text"></td>
      <td><input type="text"></td>
      <td><input type="email"></td>
    </tr>
  </table>

  <!-- Educational Details -->
  <div class="subhead">Educational Details</div>
  <table>
    <tr>
      <th colspan="4">SSC/CBSE etc</th>
      <th>School of Study & Place</th>
    </tr>
    <tr>
      <td>% of Marks</td>
      <td><input type="text"></td>
      <td>GRADE</td>
      <td><input type="text"></td>
      <td><input type="text"></td>
    </tr>
    <tr>
      <th colspan="4">INTERMEDIATE / +2 / DIPLOMA</th>
      <th>College of Study & Place</th>
    </tr>
    <tr>
      <td>% of Marks</td>
      <td><input type="text"></td>
      <td>GRADE</td>
      <td><input type="text"></td>
      <td><input type="text"></td>
    </tr>
  </table>

  <!-- Entrance Exam -->
  <div class="subhead">Qualifying Examination Details</div>
  <table>
    <tr>
      <th colspan="3">EAMCET</th>
      <th colspan="3">JEE</th>
      <th colspan="3">ECET (Diploma)</th>
    </tr>
    <tr>
      <th>H T NO</th><th>YEAR</th><th>RANK</th>
      <th>H T NO</th><th>YEAR</th><th>RANK</th>
      <th>H T NO</th><th>YEAR</th><th>RANK</th>
    </tr>
    <tr>
      <td><input type="text"></td><td><input type="text"></td><td><input type="text"></td>
      <td><input type="text"></td><td><input type="text"></td><td><input type="text"></td>
      <td><input type="text"></td><td><input type="text"></td><td><input type="text"></td>
    </tr>
  </table>

  <!-- Admission -->
  <div class="subhead">Admission Details</div>
  <table>
    <tr>
      <th colspan="4">Category of Admission</th>
      <th>Nationality & Religion</th>
      <th>Caste & Category</th>
      <th>State to which belongs to</th>
    </tr>
    <tr>
      <th colspan="2">EAMCET<th>SPOT</th><th>ECET</th>
      <td><input type="text"></td>
      <td><input type="text"></td>
      </td><th>Example-AP</th>
    </tr>
    <tr>
      <th>Cat A<th>Cat B</th>
      <td><input type="text"></td>
      <td><input type="text"></td>
      <td><input type="text"></td>
      <td><input type="text"></td>
      <td><input type="text"></td>

    </tr>

  </table>

  <table>
    <tr>
      <th colspan="4">Availing AP Govt. Fee Reimbursement Scheme</th>
      <th>YES</th><td><input type="checkbox"></td>
      <th>NO</th><td><input type="checkbox"></td>
      <th>EWS</th><td><input type="checkbox"></td>
    </tr>
  </table>

  <!-- Parents -->
  <div class="subhead">Details of Parents</div>
  <table>
    <tr>
      <th>Father's Name</th>
      <th>Mother's Name</th>
    </tr>
    <tr>
      <td><input type="text"></td>
      <td><input type="text"></td>
    </tr>
  </table>
  <table>
    <tr>
      <th>Qualification</th><td><input type="text"></td>
      <th>Qualification</th><td><input type="text"></td>
    </tr>
    <tr>
      <th>Occupation</th><td><input type="text"></td>
      <th>Occupation</th><td><input type="text"></td>
    </tr>
    <tr>
      <th>Annual Income</th><td><input type="text"></td>
      <th>Annual Income</th><td><input type="text"></td>
    </tr>
    <tr>
      <th>Land Line (Off/Res)</th><td><input type="text"></td>
      <th>Land Line (Off/Res)</th><td><input type="text"></td>
    </tr>
    <tr>
      <th>Mobile No.</th><td><input type="text"></td>
      <th>Mobile No.</th><td><input type="text"></td>
    </tr>
    <tr>
      <th>e-mail ID</th><td><input type="text"></td>
      <th>e-mail ID</th><td><input type="text"></td>
    </tr>
  </table>

  <!-- Address -->
  <table>
    <tr>
      <th>PERMANENT ADDRESS</th>
      <th>CONTACT ADDRESS</th>
    </tr>
    <tr>
      <td><textarea rows="3"></textarea></td>
      <td><textarea rows="3"></textarea></td>
    </tr>
  </table>

  <!-- Hostel -->
  <table>
    <tr>
      <th colspan="2">DETAILS OF HOSTEL (if any)</th>
      <th colspan="2">Details of LOCAL Guardian</th>
    </tr>
    <tr>
      <th>Hostel Name</th><td><input type="text"></td>
      <th>Name</th><td><input type="text"></td>
    </tr>
    <tr>
      <th>Address</th><td><textarea rows="2"></textarea></td>
      <th>Address</th><td><textarea rows="2"></textarea></td>
    </tr>
    <tr>
      <th>Phone No.</th><td><input type="text"></td>
      <th>Phone No.</th><td><input type="text"></td>
    </tr>
    <tr>
      <th>Mobile No.</th><td><input type="text"></td>
      <th>Mobile No.</th><td><input type="text"></td>
    </tr>
  </table>
</body>
</html>