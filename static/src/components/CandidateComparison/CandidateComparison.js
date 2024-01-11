/** @odoo-module **/
import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

export class CandidateComparison extends Component {
    setup() {
        this.state = useState({
            clientName: "Nombre del Cliente",
            position: "Posición Deseada",
            date: "Fecha Actual",
            candidates: [
                {   
                    name: "Juan Pérez",
                    age: 30,
                    maritalStatus: "Soltero",
                    hasChildren: "No",
                    university: "UCA",
                    nationality: "Nicaragüense",
                    residence: "Managua",
                    language: "Español",
                    photo: "https://scontent.fmga8-1.fna.fbcdn.net/v/t39.30808-6/419101307_910334860820069_8926566095950332489_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=3635dc&_nc_ohc=Yd2mLk21YnwAX90VkNt&_nc_ht=scontent.fmga8-1.fna&oh=00_AfCBEXT18rwUzmsYho-aLvA2S_s7rcEGNwXITxXDOb7PtA&oe=65A46134",
                    cvLink: "ruta/al/cv1.pdf"
                    // Añade más datos según necesites
                },
                {
                    name: "María Gómez",
                    age: 28,
                    maritalStatus: "Casada",
                    hasChildren: "Sí",
                    university: "UNAN",
                    nationality: "Nicaragüense",
                    residence: "León",
                    language: "Español",
                    photo: "https://scontent.fmga8-1.fna.fbcdn.net/v/t39.30808-6/419123991_910337194153169_2817824128026953007_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=3635dc&_nc_ohc=MQEUUl1PSggAX_wCHcj&_nc_ht=scontent.fmga8-1.fna&oh=00_AfBPk28EI85gSX5cGbYG-1xMS4UCST0vVzwYNJjv0SzUSA&oe=65A53154",
                    cvLink: "ruta/al/cv2.pdf"
                    // Añade más datos según necesites
                }
            ],
            requiredProfile: {
                studies: "Detalles de los estudios requeridos",
            },
            interviewerNotes: "Comentarios del entrevistador",
            salaryExpectation: "Detalles de la expectativa salarial"
        });

        this.orm = useService("orm");   
    }
}

CandidateComparison.template = "headhunting.CandidateComparison";

registry.category('actions').add('headhunting.action_candidate_comparison', CandidateComparison);