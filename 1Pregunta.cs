namespace EstudianteApp.Entities
{
    public class Estudiante
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
    }
}



using EstudianteApp.Entities;
using System.Collections.Generic;

namespace EstudianteApp.Data
{
    public class EstudianteRepository
    {
        public List<Estudiante> GetAllEstudiantes()
        {
            // Simulación de datos
            return new List<Estudiante>
            {
                new Estudiante { Id = 1, Name = "John Doe", Email = "john.doe@example.com" },
                new Estudiante { Id = 2, Name = "Jane Smith", Email = "jane.smith@example.com" }
            };
        }
    }
}

using EstudianeApp.Data;
using EstudianteApp.Entities;
using System.Collections.Generic;

namespace EstudianteApp.Business
{
    public class EstudianteService
    {
        private EstudianteRepository estudianteRepository;

        public EstudianteService()
        {
            estudianteRepository = new EstudianteRepository();
        }

        public List<Estudiante> GetAllEstudiantes()
        {
            return estudianteRepository.GetAllEstudiantes();
        }
    }
}



namespace EstudianteApp
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridView1
            // 
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(12, 12);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.Size = new System.Drawing.Size(776, 426);
            this.dataGridView1.TabIndex = 0;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.dataGridView1);
            this.Name = "Form1";
            this.Text = "StudentApp";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);

        }

        private System.Windows.Forms.DataGridView dataGridView1;
    }
}

