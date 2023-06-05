from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Faateh@localhost:5432/postgres'
app.config['SQLALCHEMY_BINDS'] = {
    'database1': 'postgresql://postgres:Faateh123@localhost:5432/development',
    'database2': 'postgresql://postgres:Faateh123@localhost:5432/tech_support_test',
    'database3': 'postgresql://postgres:Faateh123@localhost:5432/trials_test',
    'database4': 'postgresql://postgres:Faateh123@localhost:5432/projects_test'
}
db = SQLAlchemy(app)

class RmaTool(db.Model):
    __bind_key__ = 'database1'
    __tablename__ = 'rma_test'
    # Define your model fields and relationships
    MAT_RMA_ID = db.Column(db.String(100), primary_key=True)
    DATE_RMA_RECEIVED = db.Column(db.String(50), nullable=False)
    CUSTOMER_OPERATOR = db.Column(db.String(1000), nullable=False)
    SUBCONTRACTOR = db.Column(db.String(1000), nullable=True)
    MATSING_REP = db.Column(db.String(50), nullable=True)
    ANTENNA_MODEL_NO_SERIAL_NO = db.Column(db.String(200), nullable=False)
    STATUS = db.Column(db.String(50), nullable=True)
    ISSUE = db.Column(db.String(500), nullable=True)
    RESOLUTION = db.Column(db.String(1000), nullable=True)
    DATE_RESOLVED = db.Column(db.String(25), nullable=True)
    DEFECTIVE_UNITS_LOCATION_INFO = db.Column(db.String(200), nullable=True)
    NEXT_STEPS = db.Column(db.String(200), nullable=True)
    requestor_company_name = db.Column(db.String(255), nullable=True)
    requestor_contact_name = db.Column(db.String(255), nullable=True)
    requestor_email_address = db.Column(db.String(255), nullable=True)
    requestor_phone_number = db.Column(db.String(255), nullable=True)
    requestor_role = db.Column(db.String(255), nullable=True)
    original_po_number = db.Column(db.String(255), nullable=True)
    model_numbers_of_antennas_being_returned = db.Column(db.String(255), nullable=True)
    serial_numbers_of_antennas_being_returned = db.Column(db.String(255), nullable=True)
    problem_description = db.Column(db.String(5000), nullable=True)
    replacement_shipment_contact_name = db.Column(db.String(255), nullable=True)
    replacement_shipment_contact_phone_number = db.Column(db.String(255), nullable=True)
    replacement_shipment_email_address = db.Column(db.String(255), nullable=True)
    replacement_shipment_receiving_location = db.Column(db.String(255), nullable=True)
    replacement_shipment_instructions = db.Column(db.String(255), nullable=True)
    company = db.Column(db.String(255), nullable=True)
    contact_person_for_pick_up = db.Column(db.String(255), nullable=True)
    pick_up_location_of_antenna_to_be_returned = db.Column(db.String(255), nullable=True)
    contact_email_for_pick_up = db.Column(db.String(255), nullable=True)
    contact_phone_number_for_pick_up = db.Column(db.String(255), nullable=True)
    date_ready_for_pick_up = db.Column(db.String(255), nullable=True)
    wireless_operator_company_name = db.Column(db.String(255), nullable=True)
    wireless_operator_contact_name = db.Column(db.String(255), nullable=True)
    wireless_operator_email_address = db.Column(db.String(255), nullable=True)
    wireless_operator_phone_number = db.Column(db.String(255), nullable=True)
    matsing_rep_company_name = db.Column(db.String(255), nullable=True)
    matsing_rep_contact_name = db.Column(db.String(255), nullable=True)
    matsing_rep_email_address = db.Column(db.String(255), nullable=True)
    matsing_rep_phone_number = db.Column(db.String(255), nullable=True)
    is_this_a_new_issue = db.Column(db.String(255), nullable=True)
    is_this_an_event_site = db.Column(db.String(255), nullable=True)
    is_this_a_macro_site = db.Column(db.String(255), nullable=True)
    image = db.Column(db.LargeBinary, nullable=True)
    image_2 = db.Column(db.LargeBinary, nullable=True)
    image_3 = db.Column(db.LargeBinary, nullable=True)
    user = db.Column(db.String(25), nullable=True)
    unique_key = db.Column(db.String(50), nullable=True)
    order_no = db.Column(db.String(25), nullable=True)
    date_updated = db.Column(db.String(25), nullable=True)
    days_since_rma = db.Column(db.String(10), nullable=True)
    summary_status = db.Column(db.String(200), nullable=True)
    open_closed = db.Column(db.String(25), nullable=True)
    rma_summary_issue = db.Column(db.String(50), nullable=True)
    rma_summary_country = db.Column(db.String(50), nullable=True)
    rma_summary_city = db.Column(db.String(50), nullable=True)
    rma_summary_field_engineer = db.Column(db.String(50), nullable=True)
    filename_1 = db.Column(db.String(1000), nullable=True)
    filename_2 = db.Column(db.String(1000), nullable=True)
    filename_3 = db.Column(db.String(1000), nullable=True)
    s3url1 = db.Column(db.String(300), nullable=True)
    s3url2 = db.Column(db.String(300), nullable=True)
    s3url3 = db.Column(db.String(300), nullable=True)
    priority = db.Column(db.String(200), nullable=True)
    deadline = db.Column(db.String(200), nullable=True)
    assigned_to = db.Column(db.String(50), nullable=True)
    parts_ordered = db.Column(db.String(500), nullable=True)
    parts_required = db.Column(db.String(500), nullable=True)
    parts_delivery_eat = db.Column(db.String(500), nullable=True)
    site_name = db.Column(db.String(255), nullable=True)
    summary_model_no = db.Column(db.String(1000), nullable=True)
    summary_serial_no = db.Column(db.String(1000), nullable=True)
    replacement_unit_delivered_date = db.Column(db.String(100), nullable=True)
    defective_unit_returned_date = db.Column(db.String(100), nullable=True)
    inspection_report_status = db.Column(db.String(100), nullable=True)
    queue = db.Column(db.String(100), nullable=True)
    qc_report_status = db.Column(db.String(255), nullable=True)
    under_warranty = db.Column(db.String(255), nullable=True)
    rep_firm = db.Column(db.String(100), nullable=True)
    site_name_form = db.Column(db.String(255), nullable=True)
    is_there_physical_damage = db.Column(db.String(25), nullable=True)
    radio_vender = db.Column(db.String(255), nullable=True)
    radio_model_number = db.Column(db.String(255), nullable=True)
    new_repeat = db.Column(db.String(255), nullable=True)
    replacement_unit_model_no = db.Column(db.String(500), nullable=True)

class TechSupport(db.Model):
    __bind_key__ = 'database2'
    # Define your model fields and relationships
    __tablename__ = 'Ticket'
    ticket_id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    email = db.Column(db.String(100))
    subject = db.Column(db.String(50))
    issue = db.Column(db.String(5000))
    date_submitted = db.Column(db.String(50))
    company_name = db.Column(db.String(255))
    antenna_model_number = db.Column(db.String(255))
    status = db.Column(db.String(255))
    resolution_date = db.Column(db.String(255))
    resolution_eta = db.Column(db.String(255))
    Priority = db.Column(db.String(255))

class Trials(db.Model):
    __bind_key__ = 'database3'
    # Define your model fields and relationships
    __tablename__ = 'trials'
    trial_id = db.Column(db.String(50), primary_key=True)
    trial_year = db.Column(db.String(50))
    country = db.Column(db.String(50))
    operator = db.Column(db.String(255))
    rep_company = db.Column(db.String(255))
    venue = db.Column(db.String(255))
    status = db.Column(db.String(255))
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))
    result = db.Column(db.String(500))
    antenna_status = db.Column(db.String(255))
    notes = db.Column(db.String(1000))
    last_updated = db.Column(db.String(500))
    antenna_readiness_eta = db.Column(db.String(255))
    antenna_shipment_eta = db.Column(db.String(255))
    aos_status = db.Column(db.String(500))
    model_qty = db.Column(db.String(500))
    shipped_model_serial = db.Column(db.String(500))

class Projects(db.Model):
    __bind_key__ = 'database4'
    # Define your model fields and relationships
    __tablename__ = 'projects'
    project_id = db.Column(db.String(50), primary_key=True)
    project_year = db.Column(db.String(50))
    country = db.Column(db.String(50))
    status = db.Column(db.String(255))
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))
    result = db.Column(db.String(500))
    notes = db.Column(db.String(1000))
    last_updated = db.Column(db.String(500))

@app.route('/')
def hello_world():
    # rows = RmaTool.query.all()
    # for row in rows:
    #     print(row.MAT_RMA_ID)
    return render_template("home.html")



if __name__ == '__main__':
    app.run()
