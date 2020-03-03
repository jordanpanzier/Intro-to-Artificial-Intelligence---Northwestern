(define (domain sokorobotto)
    (:requirements :typing)
    (:types shipment - object
            order - object
            location - object
            saleitem - object
            robot - moveable
            pallette - moveable
            )
    (:predicates (includes ?x - shipment ?y - saleitem)
                 (ships ?x - shipment ?y - order)
                 (orders ?x - order ?y - saleitem)
                 (unstarted ?x - shipment)
                 (packing-location ?x - location)
                 (available ?x - location)
                 (contains ?x - pallette ?y - saleitem)
                 (free ?x - robot)
                 (connected ?x - location ?y - location)
                 (at ?x - moveable ?y - location)
                 (no-robot ?x - location)
                 (no-pallette ?x - location)
                 (has-pallette ?x - robot ?y - pallette)
                 (has-robot ?x - pallette ?y - robot)
                 )

    (:action move-robot-no-pall
            :parameters (?r - robot
                         ?loc1 - location
                         ?loc2 - location)
            :precondition (and (connected ?loc1 ?loc2)
                               (free ?r)
                               (at ?r ?loc1)
                               (no-robot ?loc2))
            :effect (and (at ?r ?loc2)
                         (no-robot ?loc1)
                         (not (at ?r ?loc1))
                         (not (no-robot ?loc2)))
            )
    (:action move-robot-yes-pall
            :parameters (?r - robot
                         ?loc1 - location
                         ?loc2 - location
                         ?p - pallette)
            :precondition (and (connected ?loc1 ?loc2)
                               (has-pallette ?r ?p)
                               (at ?r ?loc1)
                               (at ?p ?loc1)
                               (no-robot ?loc2)
                               (no-pallette ?loc2))
            :effect (and (at ?r ?loc2)
                         (at ?p ?loc2)
                         (no-robot ?loc1)
                         (no-pallette ?loc1)
                         (not (at ?r ?loc1))
                         (not (at ?p ?loc1))
                         (not (no-robot ?loc2))
                         (not (no-pallette ?loc2)))
            )
    (:action get-pall
            :parameters (?r - robot
                         ?p - pallette
                         ?loc1 - location)
            :precondition (and (at ?r ?loc1)
                               (at ?p ?loc1)
                               (free ?r))
            :effect (and (has-pallette ?r ?p)
                         (has-robot ?p ?r)
                         (not (free ?r)))
            )
    (:action drop-pall
            :parameters (?r - robot
                         ?p - pallette
                         ?loc1 - location)
            :precondition (and (at ?r ?loc1)
                               (at ?p ?loc1)
                               (has-pallette ?r ?p)
                               (has-robot ?p ?r))
            :effect (and (not (has-pallette ?r ?p))
                         (not (has-robot ?p ?r))
                         (free ?r))
            )
    (:action pack
            :parameters (?r - robot
                         ?p - pallette
                         ?loc1 - location
                         ?o - order
                         ?i - saleitem
                         ?s - shipment)
            :precondition (and (packing-location ?loc1)
                               (contains ?p ?i)
                               (orders ?o ?i)
                               (ships? ?s ?o)
                               (at ?p ?loc1)
                               (not (includes ?s ?i))
                            )
            :effect (and (includes ?s ?i)
                         (not (contains ?p ?i))
                         (not (unstarted ?s)))

            )


)















